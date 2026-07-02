#!/usr/bin/env python3
"""Infrastructure health checker : reads config.yml, runs checks, outputs reports."""

import json
import socket
import ssl
import sys
import time
from datetime import datetime, timezone
from pathlib import Path

import requests
import yaml


def load_config(path="config.yml"):
    with open(path) as f:
        return yaml.safe_load(f)


def check_http(check):
    result = {
        "name": check["name"],
        "type": "http",
        "target": check["url"],
        "expected_status": check["expected_status"],
    }
    try:
        start = time.time()
        resp = requests.get(check["url"], timeout=check.get("timeout", 10), allow_redirects=True)
        elapsed = round(time.time() - start, 3)
        result["actual_status"] = resp.status_code
        result["response_time"] = elapsed
        result["pass"] = resp.status_code == check["expected_status"]
    except requests.RequestException as e:
        result["actual_status"] = None
        result["response_time"] = None
        result["pass"] = False
        result["error"] = str(e)
    return result


def check_tls(check):
    result = {
        "name": check["name"],
        "type": "tls",
        "target": f"{check['host']}:{check.get('port', 443)}",
    }
    try:
        ctx = ssl.create_default_context()
        with ctx.wrap_socket(socket.socket(), server_hostname=check["host"]) as s:
            s.settimeout(10)
            s.connect((check["host"], check.get("port", 443)))
            cert = s.getpeercert()
        expiry = datetime.strptime(cert["notAfter"], "%b %d %H:%M:%S %Y %Z").replace(tzinfo=timezone.utc)
        days_left = (expiry - datetime.now(timezone.utc)).days
        result["expiry"] = expiry.isoformat()
        result["days_left"] = days_left
        result["pass"] = days_left > check.get("warn_days", 30)
    except Exception as e:
        result["expiry"] = None
        result["days_left"] = None
        result["pass"] = False
        result["error"] = str(e)
    return result


def check_tcp(check):
    result = {
        "name": check["name"],
        "type": "tcp",
        "target": f"{check['host']}:{check['port']}",
    }
    try:
        start = time.time()
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(check.get("timeout", 5))
        s.connect((check["host"], check["port"]))
        elapsed = round(time.time() - start, 3)
        s.close()
        result["response_time"] = elapsed
        result["pass"] = True
    except Exception as e:
        result["response_time"] = None
        result["pass"] = False
        result["error"] = str(e)
    return result


def check_dns(check):
    result = {
        "name": check["name"],
        "type": "dns",
        "target": check["domain"],
        "expected_ip": check.get("expected_ip"),
    }
    try:
        resolved = socket.gethostbyname(check["domain"])
        result["resolved_ip"] = resolved
        if check.get("expected_ip"):
            result["pass"] = resolved == check["expected_ip"]
        else:
            result["pass"] = True
    except Exception as e:
        result["resolved_ip"] = None
        result["pass"] = False
        result["error"] = str(e)
    return result


def run_all(config):
    results = []
    for check in config.get("checks", {}).get("http", []):
        results.append(check_http(check))
    for check in config.get("checks", {}).get("tls", []):
        results.append(check_tls(check))
    for check in config.get("checks", {}).get("tcp", []):
        results.append(check_tcp(check))
    for check in config.get("checks", {}).get("dns", []):
        results.append(check_dns(check))
    return results


def generate_json_report(results, path="reports/latest.json"):
    report = {
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "total": len(results),
        "passed": sum(1 for r in results if r["pass"]),
        "failed": sum(1 for r in results if not r["pass"]),
        "results": results,
    }
    Path(path).parent.mkdir(parents=True, exist_ok=True)
    with open(path, "w") as f:
        json.dump(report, f, indent=2)
    return report


def generate_md_report(report, path="reports/latest.md"):
    ts = report["timestamp"]
    lines = [
        f"# Infrastructure Health Report",
        f"",
        f"**Date** : {ts}",
        f"",
        f"**Résultat** : {report['passed']}/{report['total']} checks OK",
        f"",
        f"| Check | Type | Cible | Statut | Détail |",
        f"|---|---|---|---|---|",
    ]
    for r in report["results"]:
        status = "✅" if r["pass"] else "❌"
        detail = ""
        if r["type"] == "http":
            detail = f"HTTP {r.get('actual_status', 'N/A')} — {r.get('response_time', 'N/A')}s"
        elif r["type"] == "tls":
            detail = f"Expire dans {r.get('days_left', 'N/A')} jours"
        elif r["type"] == "tcp":
            detail = f"{r.get('response_time', 'N/A')}s"
        elif r["type"] == "dns":
            detail = f"Résolu: {r.get('resolved_ip', 'N/A')}"
        if "error" in r:
            detail = f"Erreur: {r['error'][:60]}"
        lines.append(f"| {r['name']} | {r['type']} | {r['target']} | {status} | {detail} |")

    Path(path).parent.mkdir(parents=True, exist_ok=True)
    with open(path, "w") as f:
        f.write("\n".join(lines) + "\n")


def main():
    config = load_config()
    results = run_all(config)
    report = generate_json_report(results)
    generate_md_report(report)

    failed = report["failed"]
    print(f"Checks: {report['passed']}/{report['total']} passed")
    if failed > 0:
        print(f"WARN: {failed} check(s) failed")
        sys.exit(1)
    sys.exit(0)


if __name__ == "__main__":
    main()