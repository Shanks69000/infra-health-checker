# Infrastructure Health Report

**Date** : 2026-08-06T23:55:04.282718+00:00

**Résultat** : 8/8 checks OK

| Check | Type | Cible | Statut | Détail |
|---|---|---|---|---|
| GitHub | http | https://github.com | ✅ | HTTP 200 — 0.172s |
| Docker Hub | http | https://hub.docker.com | ✅ | HTTP 200 — 0.247s |
| Terraform Registry | http | https://registry.terraform.io | ✅ | HTTP 200 — 0.121s |
| GitHub TLS | tls | github.com:443 | ✅ | Expire dans 55 jours |
| Docker Hub TLS | tls | hub.docker.com:443 | ✅ | Expire dans 58 jours |
| GitHub SSH | tcp | github.com:22 | ✅ | 0.026s |
| Google DNS | tcp | 8.8.8.8:53 | ✅ | 0.016s |
| GitHub DNS | dns | github.com | ✅ | Résolu: 140.82.113.3 |
