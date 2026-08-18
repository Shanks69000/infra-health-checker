# Infrastructure Health Report

**Date** : 2026-08-18T12:38:25.061663+00:00

**Résultat** : 8/8 checks OK

| Check | Type | Cible | Statut | Détail |
|---|---|---|---|---|
| GitHub | http | https://github.com | ✅ | HTTP 200 — 0.165s |
| Docker Hub | http | https://hub.docker.com | ✅ | HTTP 200 — 0.171s |
| Terraform Registry | http | https://registry.terraform.io | ✅ | HTTP 200 — 0.132s |
| GitHub TLS | tls | github.com:443 | ✅ | Expire dans 43 jours |
| Docker Hub TLS | tls | hub.docker.com:443 | ✅ | Expire dans 85 jours |
| GitHub SSH | tcp | github.com:22 | ✅ | 0.03s |
| Google DNS | tcp | 8.8.8.8:53 | ✅ | 0.015s |
| GitHub DNS | dns | github.com | ✅ | Résolu: 140.82.114.3 |
