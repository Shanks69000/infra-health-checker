# Infrastructure Health Report

**Date** : 2026-11-23T17:18:02.648017+00:00

**Résultat** : 8/8 checks OK

| Check | Type | Cible | Statut | Détail |
|---|---|---|---|---|
| GitHub | http | https://github.com | ✅ | HTTP 200 — 0.09s |
| Docker Hub | http | https://hub.docker.com | ✅ | HTTP 200 — 0.163s |
| Terraform Registry | http | https://registry.terraform.io | ✅ | HTTP 200 — 0.113s |
| GitHub TLS | tls | github.com:443 | ✅ | Expire dans 65 jours |
| Docker Hub TLS | tls | hub.docker.com:443 | ✅ | Expire dans 68 jours |
| GitHub SSH | tcp | github.com:22 | ✅ | 0.015s |
| Google DNS | tcp | 8.8.8.8:53 | ✅ | 0.007s |
| GitHub DNS | dns | github.com | ✅ | Résolu: 57.166.80.144 |
