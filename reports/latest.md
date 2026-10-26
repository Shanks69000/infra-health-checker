# Infrastructure Health Report

**Date** : 2026-10-26T22:15:23.769884+00:00

**Résultat** : 8/8 checks OK

| Check | Type | Cible | Statut | Détail |
|---|---|---|---|---|
| GitHub | http | https://github.com | ✅ | HTTP 200 — 0.337s |
| Docker Hub | http | https://hub.docker.com | ✅ | HTTP 200 — 0.223s |
| Terraform Registry | http | https://registry.terraform.io | ✅ | HTTP 200 — 0.109s |
| GitHub TLS | tls | github.com:443 | ✅ | Expire dans 34 jours |
| Docker Hub TLS | tls | hub.docker.com:443 | ✅ | Expire dans 74 jours |
| GitHub SSH | tcp | github.com:22 | ✅ | 0.054s |
| Google DNS | tcp | 8.8.8.8:53 | ✅ | 0.035s |
| GitHub DNS | dns | github.com | ✅ | Résolu: 140.82.114.4 |
