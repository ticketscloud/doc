#!/bin/sh

set -e -x

REGISTRY=cr.yandex/crp1ijd2b1iedqvsiro7
TAG=$(cat build/version)

(cd deploy/k8s && kustomize edit set image api-docs=${REGISTRY}/api-docs:${TAG})
