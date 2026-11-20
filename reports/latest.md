# Infrastructure Health Report

**Date** : 2026-11-20T23:39:15.794575+00:00

**Résultat** : 8/8 checks OK

| Check | Type | Cible | Statut | Détail |
|---|---|---|---|---|
| GitHub | http | https://github.com | ✅ | HTTP 200 — 0.092s |
| Docker Hub | http | https://hub.docker.com | ✅ | HTTP 200 — 0.16s |
| Terraform Registry | http | https://registry.terraform.io | ✅ | HTTP 200 — 0.103s |
| GitHub TLS | tls | github.com:443 | ✅ | Expire dans 68 jours |
| Docker Hub TLS | tls | hub.docker.com:443 | ✅ | Expire dans 70 jours |
| GitHub SSH | tcp | github.com:22 | ✅ | 0.014s |
| Google DNS | tcp | 8.8.8.8:53 | ✅ | 0.006s |
| GitHub DNS | dns | github.com | ✅ | Résolu: 48.202.91.176 |
