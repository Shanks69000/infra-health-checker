# Infrastructure Health Report

**Date** : 2026-08-15T12:30:28.894488+00:00

**Résultat** : 8/8 checks OK

| Check | Type | Cible | Statut | Détail |
|---|---|---|---|---|
| GitHub | http | https://github.com | ✅ | HTTP 200 — 0.34s |
| Docker Hub | http | https://hub.docker.com | ✅ | HTTP 200 — 0.206s |
| Terraform Registry | http | https://registry.terraform.io | ✅ | HTTP 200 — 0.137s |
| GitHub TLS | tls | github.com:443 | ✅ | Expire dans 46 jours |
| Docker Hub TLS | tls | hub.docker.com:443 | ✅ | Expire dans 88 jours |
| GitHub SSH | tcp | github.com:22 | ✅ | 0.066s |
| Google DNS | tcp | 8.8.8.8:53 | ✅ | 0.002s |
| GitHub DNS | dns | github.com | ✅ | Résolu: 140.82.112.3 |
