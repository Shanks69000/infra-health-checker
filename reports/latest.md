# Infrastructure Health Report

**Date** : 2026-10-23T16:24:07.106485+00:00

**Résultat** : 8/8 checks OK

| Check | Type | Cible | Statut | Détail |
|---|---|---|---|---|
| GitHub | http | https://github.com | ✅ | HTTP 200 — 0.224s |
| Docker Hub | http | https://hub.docker.com | ✅ | HTTP 200 — 0.236s |
| Terraform Registry | http | https://registry.terraform.io | ✅ | HTTP 200 — 0.126s |
| GitHub TLS | tls | github.com:443 | ✅ | Expire dans 37 jours |
| Docker Hub TLS | tls | hub.docker.com:443 | ✅ | Expire dans 77 jours |
| GitHub SSH | tcp | github.com:22 | ✅ | 0.032s |
| Google DNS | tcp | 8.8.8.8:53 | ✅ | 0.017s |
| GitHub DNS | dns | github.com | ✅ | Résolu: 140.82.112.4 |
