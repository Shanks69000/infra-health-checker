# Infrastructure Health Report

**Date** : 2026-09-02T20:28:16.825184+00:00

**Résultat** : 8/8 checks OK

| Check | Type | Cible | Statut | Détail |
|---|---|---|---|---|
| GitHub | http | https://github.com | ✅ | HTTP 200 — 0.043s |
| Docker Hub | http | https://hub.docker.com | ✅ | HTTP 200 — 0.253s |
| Terraform Registry | http | https://registry.terraform.io | ✅ | HTTP 200 — 0.17s |
| GitHub TLS | tls | github.com:443 | ✅ | Expire dans 88 jours |
| Docker Hub TLS | tls | hub.docker.com:443 | ✅ | Expire dans 69 jours |
| GitHub SSH | tcp | github.com:22 | ✅ | 0.004s |
| Google DNS | tcp | 8.8.8.8:53 | ✅ | 0.005s |
| GitHub DNS | dns | github.com | ✅ | Résolu: 20.29.134.23 |
