# Infrastructure Health Report

**Date** : 2026-11-28T01:01:46.596100+00:00

**Résultat** : 8/8 checks OK

| Check | Type | Cible | Statut | Détail |
|---|---|---|---|---|
| GitHub | http | https://github.com | ✅ | HTTP 200 — 0.15s |
| Docker Hub | http | https://hub.docker.com | ✅ | HTTP 200 — 0.154s |
| Terraform Registry | http | https://registry.terraform.io | ✅ | HTTP 200 — 0.123s |
| GitHub TLS | tls | github.com:443 | ✅ | Expire dans 60 jours |
| Docker Hub TLS | tls | hub.docker.com:443 | ✅ | Expire dans 63 jours |
| GitHub SSH | tcp | github.com:22 | ✅ | 0.031s |
| Google DNS | tcp | 8.8.8.8:53 | ✅ | 0.022s |
| GitHub DNS | dns | github.com | ✅ | Résolu: 140.82.112.4 |
