# Infrastructure Health Report

**Date** : 2026-11-15T22:26:51.015292+00:00

**Résultat** : 8/8 checks OK

| Check | Type | Cible | Statut | Détail |
|---|---|---|---|---|
| GitHub | http | https://github.com | ✅ | HTTP 200 — 0.023s |
| Docker Hub | http | https://hub.docker.com | ✅ | HTTP 200 — 0.071s |
| Terraform Registry | http | https://registry.terraform.io | ✅ | HTTP 200 — 0.028s |
| GitHub TLS | tls | github.com:443 | ✅ | Expire dans 73 jours |
| Docker Hub TLS | tls | hub.docker.com:443 | ✅ | Expire dans 75 jours |
| GitHub SSH | tcp | github.com:22 | ✅ | 0.002s |
| Google DNS | tcp | 8.8.8.8:53 | ✅ | 0.002s |
| GitHub DNS | dns | github.com | ✅ | Résolu: 140.82.114.4 |
