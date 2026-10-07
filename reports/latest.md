# Infrastructure Health Report

**Date** : 2026-10-07T12:35:48.540582+00:00

**Résultat** : 8/8 checks OK

| Check | Type | Cible | Statut | Détail |
|---|---|---|---|---|
| GitHub | http | https://github.com | ✅ | HTTP 200 — 0.321s |
| Docker Hub | http | https://hub.docker.com | ✅ | HTTP 200 — 0.365s |
| Terraform Registry | http | https://registry.terraform.io | ✅ | HTTP 200 — 0.084s |
| GitHub TLS | tls | github.com:443 | ✅ | Expire dans 53 jours |
| Docker Hub TLS | tls | hub.docker.com:443 | ✅ | Expire dans 56 jours |
| GitHub SSH | tcp | github.com:22 | ✅ | 0.051s |
| Google DNS | tcp | 8.8.8.8:53 | ✅ | 0.003s |
| GitHub DNS | dns | github.com | ✅ | Résolu: 140.82.112.3 |
