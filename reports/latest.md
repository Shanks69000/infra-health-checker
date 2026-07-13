# Infrastructure Health Report

**Date** : 2026-07-13T14:27:02.283255+00:00

**Résultat** : 8/8 checks OK

| Check | Type | Cible | Statut | Détail |
|---|---|---|---|---|
| GitHub | http | https://github.com | ✅ | HTTP 200 — 0.154s |
| Docker Hub | http | https://hub.docker.com | ✅ | HTTP 200 — 0.149s |
| Terraform Registry | http | https://registry.terraform.io | ✅ | HTTP 200 — 0.119s |
| GitHub TLS | tls | github.com:443 | ✅ | Expire dans 79 jours |
| Docker Hub TLS | tls | hub.docker.com:443 | ✅ | Expire dans 83 jours |
| GitHub SSH | tcp | github.com:22 | ✅ | 0.016s |
| Google DNS | tcp | 8.8.8.8:53 | ✅ | 0.012s |
| GitHub DNS | dns | github.com | ✅ | Résolu: 140.82.113.4 |
