# Infrastructure Health Report

**Date** : 2026-08-04T14:02:56.691518+00:00

**Résultat** : 8/8 checks OK

| Check | Type | Cible | Statut | Détail |
|---|---|---|---|---|
| GitHub | http | https://github.com | ✅ | HTTP 200 — 0.041s |
| Docker Hub | http | https://hub.docker.com | ✅ | HTTP 200 — 0.082s |
| Terraform Registry | http | https://registry.terraform.io | ✅ | HTTP 200 — 0.045s |
| GitHub TLS | tls | github.com:443 | ✅ | Expire dans 57 jours |
| Docker Hub TLS | tls | hub.docker.com:443 | ✅ | Expire dans 61 jours |
| GitHub SSH | tcp | github.com:22 | ✅ | 0.002s |
| Google DNS | tcp | 8.8.8.8:53 | ✅ | 0.002s |
| GitHub DNS | dns | github.com | ✅ | Résolu: 140.82.114.3 |
