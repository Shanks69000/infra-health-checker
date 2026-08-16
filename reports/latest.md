# Infrastructure Health Report

**Date** : 2026-08-16T01:05:20.151953+00:00

**Résultat** : 8/8 checks OK

| Check | Type | Cible | Statut | Détail |
|---|---|---|---|---|
| GitHub | http | https://github.com | ✅ | HTTP 200 — 0.135s |
| Docker Hub | http | https://hub.docker.com | ✅ | HTTP 200 — 0.117s |
| Terraform Registry | http | https://registry.terraform.io | ✅ | HTTP 200 — 0.104s |
| GitHub TLS | tls | github.com:443 | ✅ | Expire dans 45 jours |
| Docker Hub TLS | tls | hub.docker.com:443 | ✅ | Expire dans 87 jours |
| GitHub SSH | tcp | github.com:22 | ✅ | 0.016s |
| Google DNS | tcp | 8.8.8.8:53 | ✅ | 0.005s |
| GitHub DNS | dns | github.com | ✅ | Résolu: 140.82.113.4 |
