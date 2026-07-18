# Infrastructure Health Report

**Date** : 2026-07-18T07:44:08.810757+00:00

**Résultat** : 8/8 checks OK

| Check | Type | Cible | Statut | Détail |
|---|---|---|---|---|
| GitHub | http | https://github.com | ✅ | HTTP 200 — 0.151s |
| Docker Hub | http | https://hub.docker.com | ✅ | HTTP 200 — 0.358s |
| Terraform Registry | http | https://registry.terraform.io | ✅ | HTTP 200 — 0.149s |
| GitHub TLS | tls | github.com:443 | ✅ | Expire dans 74 jours |
| Docker Hub TLS | tls | hub.docker.com:443 | ✅ | Expire dans 78 jours |
| GitHub SSH | tcp | github.com:22 | ✅ | 0.018s |
| Google DNS | tcp | 8.8.8.8:53 | ✅ | 0.002s |
| GitHub DNS | dns | github.com | ✅ | Résolu: 140.82.113.3 |
