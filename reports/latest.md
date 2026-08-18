# Infrastructure Health Report

**Date** : 2026-08-18T06:42:00.415550+00:00

**Résultat** : 8/8 checks OK

| Check | Type | Cible | Statut | Détail |
|---|---|---|---|---|
| GitHub | http | https://github.com | ✅ | HTTP 200 — 0.18s |
| Docker Hub | http | https://hub.docker.com | ✅ | HTTP 200 — 0.252s |
| Terraform Registry | http | https://registry.terraform.io | ✅ | HTTP 200 — 0.149s |
| GitHub TLS | tls | github.com:443 | ✅ | Expire dans 43 jours |
| Docker Hub TLS | tls | hub.docker.com:443 | ✅ | Expire dans 85 jours |
| GitHub SSH | tcp | github.com:22 | ✅ | 0.026s |
| Google DNS | tcp | 8.8.8.8:53 | ✅ | 0.012s |
| GitHub DNS | dns | github.com | ✅ | Résolu: 140.82.113.3 |
