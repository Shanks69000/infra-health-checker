# Infrastructure Health Report

**Date** : 2026-08-27T07:07:40.323744+00:00

**Résultat** : 8/8 checks OK

| Check | Type | Cible | Statut | Détail |
|---|---|---|---|---|
| GitHub | http | https://github.com | ✅ | HTTP 200 — 0.331s |
| Docker Hub | http | https://hub.docker.com | ✅ | HTTP 200 — 0.229s |
| Terraform Registry | http | https://registry.terraform.io | ✅ | HTTP 200 — 0.129s |
| GitHub TLS | tls | github.com:443 | ✅ | Expire dans 34 jours |
| Docker Hub TLS | tls | hub.docker.com:443 | ✅ | Expire dans 76 jours |
| GitHub SSH | tcp | github.com:22 | ✅ | 0.052s |
| Google DNS | tcp | 8.8.8.8:53 | ✅ | 0.002s |
| GitHub DNS | dns | github.com | ✅ | Résolu: 140.82.113.3 |
