# Infrastructure Health Report

**Date** : 2026-11-07T04:30:51.206553+00:00

**Résultat** : 8/8 checks OK

| Check | Type | Cible | Statut | Détail |
|---|---|---|---|---|
| GitHub | http | https://github.com | ✅ | HTTP 200 — 0.127s |
| Docker Hub | http | https://hub.docker.com | ✅ | HTTP 200 — 0.15s |
| Terraform Registry | http | https://registry.terraform.io | ✅ | HTTP 200 — 0.11s |
| GitHub TLS | tls | github.com:443 | ✅ | Expire dans 81 jours |
| Docker Hub TLS | tls | hub.docker.com:443 | ✅ | Expire dans 84 jours |
| GitHub SSH | tcp | github.com:22 | ✅ | 0.017s |
| Google DNS | tcp | 8.8.8.8:53 | ✅ | 0.002s |
| GitHub DNS | dns | github.com | ✅ | Résolu: 172.182.252.133 |
