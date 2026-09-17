# Infrastructure Health Report

**Date** : 2026-09-17T10:54:35.715248+00:00

**Résultat** : 8/8 checks OK

| Check | Type | Cible | Statut | Détail |
|---|---|---|---|---|
| GitHub | http | https://github.com | ✅ | HTTP 200 — 0.039s |
| Docker Hub | http | https://hub.docker.com | ✅ | HTTP 200 — 0.15s |
| Terraform Registry | http | https://registry.terraform.io | ✅ | HTTP 200 — 0.042s |
| GitHub TLS | tls | github.com:443 | ✅ | Expire dans 73 jours |
| Docker Hub TLS | tls | hub.docker.com:443 | ✅ | Expire dans 76 jours |
| GitHub SSH | tcp | github.com:22 | ✅ | 0.002s |
| Google DNS | tcp | 8.8.8.8:53 | ✅ | 0.001s |
| GitHub DNS | dns | github.com | ✅ | Résolu: 140.82.113.3 |
