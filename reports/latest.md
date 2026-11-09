# Infrastructure Health Report

**Date** : 2026-11-09T15:04:07.017585+00:00

**Résultat** : 8/8 checks OK

| Check | Type | Cible | Statut | Détail |
|---|---|---|---|---|
| GitHub | http | https://github.com | ✅ | HTTP 200 — 0.325s |
| Docker Hub | http | https://hub.docker.com | ✅ | HTTP 200 — 0.204s |
| Terraform Registry | http | https://registry.terraform.io | ✅ | HTTP 200 — 0.104s |
| GitHub TLS | tls | github.com:443 | ✅ | Expire dans 79 jours |
| Docker Hub TLS | tls | hub.docker.com:443 | ✅ | Expire dans 82 jours |
| GitHub SSH | tcp | github.com:22 | ✅ | 0.051s |
| Google DNS | tcp | 8.8.8.8:53 | ✅ | 0.005s |
| GitHub DNS | dns | github.com | ✅ | Résolu: 140.82.114.4 |
