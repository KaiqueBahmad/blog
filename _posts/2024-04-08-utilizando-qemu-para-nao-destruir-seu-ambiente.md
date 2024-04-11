---
layout:    post
title:    "Usando QEMU para não destruir seu ambiente"
categories: default
---

## Resumo

Especialmente se você utiliza sistemas operacionais que te dão uma certa liberdade na hora de fazer modificações, é nescessário ter uma certa precaução na hora de testar coisas novas, pois apesar do pior que pode acontecer ser você ter que formatar sua máquina, ninguém quer perder um dia inteiro formatando e reconfigurando uma, se pode haver uma forma melhor de fazer testes sem se preocupar em destruir seu ambiente atual.

Esse post irá mostrar uma forma de testar alterações antes de aplica-las no seu sistema para evitar surpresas, utilizando QEMU.