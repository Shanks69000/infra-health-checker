# Infrastructure Health Report

**Date** : 2026-08-13T01:42:37.881142+00:00

**Résultat** : 7/8 checks OK

| Check | Type | Cible | Statut | Détail |
|---|---|---|---|---|
| GitHub | http | https://github.com | ❌ | Erreur: ('Connection aborted.', RemoteDisconnected('Remote end close |
| Docker Hub | http | https://hub.docker.com | ✅ | HTTP 200 — 0.79s |
| Terraform Registry | http | https://registry.terraform.io | ✅ | HTTP 200 — 0.123s |
| GitHub TLS | tls | github.com:443 | ✅ | Expire dans 48 jours |
| Docker Hub TLS | tls | hub.docker.com:443 | ✅ | Expire dans 52 jours |
| GitHub SSH | tcp | github.com:22 | ✅ | 0.003s |
| Google DNS | tcp | 8.8.8.8:53 | ✅ | 0.001s |
| GitHub DNS | dns | github.com | ✅ | Résolu: 140.82.112.4 |
