# Infrastructure Health Report

**Date** : 2026-07-19T08:11:06.014915+00:00

**Résultat** : 8/8 checks OK

| Check | Type | Cible | Statut | Détail |
|---|---|---|---|---|
| GitHub | http | https://github.com | ✅ | HTTP 200 — 0.18s |
| Docker Hub | http | https://hub.docker.com | ✅ | HTTP 200 — 0.376s |
| Terraform Registry | http | https://registry.terraform.io | ✅ | HTTP 200 — 0.12s |
| GitHub TLS | tls | github.com:443 | ✅ | Expire dans 73 jours |
| Docker Hub TLS | tls | hub.docker.com:443 | ✅ | Expire dans 77 jours |
| GitHub SSH | tcp | github.com:22 | ✅ | 0.024s |
| Google DNS | tcp | 8.8.8.8:53 | ✅ | 0.015s |
| GitHub DNS | dns | github.com | ✅ | Résolu: 140.82.114.4 |
