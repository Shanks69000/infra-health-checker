# Infrastructure Health Report

**Date** : 2026-08-27T21:41:45.525860+00:00

**Résultat** : 8/8 checks OK

| Check | Type | Cible | Statut | Détail |
|---|---|---|---|---|
| GitHub | http | https://github.com | ✅ | HTTP 200 — 0.135s |
| Docker Hub | http | https://hub.docker.com | ✅ | HTTP 200 — 0.152s |
| Terraform Registry | http | https://registry.terraform.io | ✅ | HTTP 200 — 0.115s |
| GitHub TLS | tls | github.com:443 | ✅ | Expire dans 34 jours |
| Docker Hub TLS | tls | hub.docker.com:443 | ✅ | Expire dans 75 jours |
| GitHub SSH | tcp | github.com:22 | ✅ | 0.016s |
| Google DNS | tcp | 8.8.8.8:53 | ✅ | 0.001s |
| GitHub DNS | dns | github.com | ✅ | Résolu: 172.182.252.133 |
