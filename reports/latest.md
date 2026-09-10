# Infrastructure Health Report

**Date** : 2026-09-10T15:46:56.849885+00:00

**Résultat** : 8/8 checks OK

| Check | Type | Cible | Statut | Détail |
|---|---|---|---|---|
| GitHub | http | https://github.com | ✅ | HTTP 200 — 0.041s |
| Docker Hub | http | https://hub.docker.com | ✅ | HTTP 200 — 0.098s |
| Terraform Registry | http | https://registry.terraform.io | ✅ | HTTP 200 — 0.046s |
| GitHub TLS | tls | github.com:443 | ✅ | Expire dans 80 jours |
| Docker Hub TLS | tls | hub.docker.com:443 | ✅ | Expire dans 83 jours |
| GitHub SSH | tcp | github.com:22 | ✅ | 0.002s |
| Google DNS | tcp | 8.8.8.8:53 | ✅ | 0.002s |
| GitHub DNS | dns | github.com | ✅ | Résolu: 140.82.112.3 |
