# Infrastructure Health Report

**Date** : 2026-11-02T14:41:25.143092+00:00

**Résultat** : 8/8 checks OK

| Check | Type | Cible | Statut | Détail |
|---|---|---|---|---|
| GitHub | http | https://github.com | ✅ | HTTP 200 — 0.179s |
| Docker Hub | http | https://hub.docker.com | ✅ | HTTP 200 — 0.175s |
| Terraform Registry | http | https://registry.terraform.io | ✅ | HTTP 200 — 0.088s |
| GitHub TLS | tls | github.com:443 | ✅ | Expire dans 86 jours |
| Docker Hub TLS | tls | hub.docker.com:443 | ✅ | Expire dans 89 jours |
| GitHub SSH | tcp | github.com:22 | ✅ | 0.023s |
| Google DNS | tcp | 8.8.8.8:53 | ✅ | 0.015s |
| GitHub DNS | dns | github.com | ✅ | Résolu: 140.82.114.4 |
