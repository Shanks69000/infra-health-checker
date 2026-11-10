# Infrastructure Health Report

**Date** : 2026-11-10T14:16:02.195915+00:00

**Résultat** : 8/8 checks OK

| Check | Type | Cible | Statut | Détail |
|---|---|---|---|---|
| GitHub | http | https://github.com | ✅ | HTTP 200 — 0.313s |
| Docker Hub | http | https://hub.docker.com | ✅ | HTTP 200 — 0.2s |
| Terraform Registry | http | https://registry.terraform.io | ✅ | HTTP 200 — 0.079s |
| GitHub TLS | tls | github.com:443 | ✅ | Expire dans 78 jours |
| Docker Hub TLS | tls | hub.docker.com:443 | ✅ | Expire dans 81 jours |
| GitHub SSH | tcp | github.com:22 | ✅ | 0.052s |
| Google DNS | tcp | 8.8.8.8:53 | ✅ | 0.003s |
| GitHub DNS | dns | github.com | ✅ | Résolu: 140.82.113.3 |
