# Infrastructure Health Report

**Date** : 2026-11-06T13:41:49.744081+00:00

**Résultat** : 8/8 checks OK

| Check | Type | Cible | Statut | Détail |
|---|---|---|---|---|
| GitHub | http | https://github.com | ✅ | HTTP 200 — 0.042s |
| Docker Hub | http | https://hub.docker.com | ✅ | HTTP 200 — 0.207s |
| Terraform Registry | http | https://registry.terraform.io | ✅ | HTTP 200 — 0.143s |
| GitHub TLS | tls | github.com:443 | ✅ | Expire dans 82 jours |
| Docker Hub TLS | tls | hub.docker.com:443 | ✅ | Expire dans 85 jours |
| GitHub SSH | tcp | github.com:22 | ✅ | 0.001s |
| Google DNS | tcp | 8.8.8.8:53 | ✅ | 0.006s |
| GitHub DNS | dns | github.com | ✅ | Résolu: 20.29.134.23 |
