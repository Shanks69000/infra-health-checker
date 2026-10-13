# Infrastructure Health Report

**Date** : 2026-10-13T22:15:25.690584+00:00

**Résultat** : 8/8 checks OK

| Check | Type | Cible | Statut | Détail |
|---|---|---|---|---|
| GitHub | http | https://github.com | ✅ | HTTP 200 — 0.217s |
| Docker Hub | http | https://hub.docker.com | ✅ | HTTP 200 — 0.216s |
| Terraform Registry | http | https://registry.terraform.io | ✅ | HTTP 200 — 0.111s |
| GitHub TLS | tls | github.com:443 | ✅ | Expire dans 47 jours |
| Docker Hub TLS | tls | hub.docker.com:443 | ✅ | Expire dans 87 jours |
| GitHub SSH | tcp | github.com:22 | ✅ | 0.033s |
| Google DNS | tcp | 8.8.8.8:53 | ✅ | 0.019s |
| GitHub DNS | dns | github.com | ✅ | Résolu: 140.82.113.4 |
