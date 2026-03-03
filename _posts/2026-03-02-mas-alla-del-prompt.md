---
layout: default
title: "Más allá del prompt: Construyendo software con intencionalidad"
lang: es
---

# Más allá del prompt: Construyendo software con intencionalidad

*This post is also available in [English](/2026/03/02/beyond-the-prompt-en.html).*

Desde que decidí [dar el primer paso](/2026/02/18/el-primer-paso.html) y soltar las estructuras conocidas, mi obsesión ha sido una sola: cómo no perder el sentido del oficio en una época donde la producción es casi infinita. La escritura de código dejó de ser un tallado manual para convertirse en una operación de maquinaria pesada, pero el problema es que hoy estamos operando esas máquinas sin planos y a oscuras.

Podemos levantar estructuras a una velocidad terminal, pero esa velocidad es una trampa. Sin un diseño claro, terminamos acumulando escombros digitales más rápido de lo que podemos entenderlos. En un post de Charly sobre [Walk this WAI](https://charly-vibes.github.io/microdancing/es/posts/walk-this-wai.html), se habla de la filosofía de la intencionalidad y de por qué no tiene sentido insistir en el trabajo a pulso para tareas que la máquina ya resolvió. Hoy quiero bajar a algo concreto y mostrar cómo se ve, paso a paso, el flujo de trabajo que estoy implementando.

#### **El problema de la automatización ciega**

El error más común hoy es tratar a estas herramientas como un martillo automático que no necesita planos. Si le pedís código sin contexto, te devuelve una estructura que se sostiene por puro azar. El verdadero salto de calidad no ocurre en el simple *prompting*[^incitaciones], sino en el diseño de un ecosistema de trabajo robusto[^aix].

Para que la máquina labure con nosotros y no contra nosotros, primero hay que construir la infraestructura donde el sistema pueda **resonar**[^resonant-coding]. No es solo tirar comandos; es armar un entorno diseñado específicamente para que nuestra intención no se pierda en el ruido. 

Acá es donde entra **WAI**[^wai]. A medida que trabajamos, la IA genera un montón de artefactos de conocimiento —research, detalles de uso, decisiones técnicas— que suelen quedar desparramados. WAI nace para orquestar todo eso, asegurando que las buenas prácticas y las definiciones de calidad no sean algo que "hay que acordarse de hacer", sino que estén integradas por diseño en el flujo de producción.

Recién sobre esta base de control y orquestación podemos aplicar los cinco momentos innegociables de mi flujo:

#### **Fase 1: Auditoría y Mapeo**
Antes de mover un solo ladrillo, hay que entender qué hay construido: tanto en las especificaciones como en el código real. Es una auditoría forense para saber dónde estamos parados. Este es el primer **guardrail**: si no tenés claros los cimientos, no podés proyectar ninguna reforma seria.

#### **Fase 2: El Diseño del Delta (La Propuesta)**
Con el mapa listo, definimos qué vamos a tocar y cómo vamos a validar que el cambio sea consistente. Usamos **OpenSpec**[^openspec] para generar una propuesta que incluya el diseño de los tests. 

Acá es donde aplicamos el primer gran filtro de **backpressure**: sometemos la propuesta a la **Regla de los 5**[^rule5] y a protocolos de revisión especializados[^incitaciones-review]. Si el diseño no convence o tiene grietas, **vuelve a boxes** sin vueltas. No avanzamos hasta que la intención esté blindada; corregir acá es casi gratis.

#### **Fase 3: Fragmentación Atómica (Beads)**
Una vez que la propuesta está firme y revisada, la desarmamos en unidades mínimas de trabajo: los **beads**[^beads]. Creamos tickets con sus dependencias claras para que puedan laburarse de manera autónoma. 

#### **Fase 4: Refinamiento de la Obra (Revisión de Tickets)**
Antes de implementar, volvemos a pasar el peine fino. Revisamos los tickets en conjunto aplicando nuevamente la **Regla de los 5**. Es el momento de pulir cada detalle; el sistema nos obliga a alcanzar la excelencia antes de que la máquina empiece a producir código.

#### **Fase 5: Implementación y Cierre**
Recién ahora implementamos, ticket por ticket. Cada uno se cierra con su propia revisión final para asegurar que lo que se construyó encaja perfecto en el hueco que diseñamos originalmente.

---

#### **El valor del oficio en la era de la IA**

Muchos me preguntan si este flujo de trabajo deja de lado la experiencia técnica. Mi respuesta es que la potencia ahora más que nunca. Para dirigir a la máquina, necesitás saber qué pedir, cómo evaluar la arquitectura y dónde están los bordes peligrosos de la tecnología.

Pero este camino también funciona a la inversa: es la llave para que personas sin un trasfondo técnico puedan empezar a construir. **Hoy ya no necesitás saber programar** en el sentido tradicional para levantar un sistema, pero lo que sí es innegociable es seguir una metodología clara. Mi objetivo es darle a esos creadores el rigor y los procesos necesarios para que su visión no se diluya y termine convertida en una estructura frágil.

Como dice el post de Charly, la respuesta ética a la hiper-velocidad de la IA es el **antídoto de la pausa**: producir menos, pero pensar mucho más. Este es el núcleo de mi nueva etapa como consultor: ayudar a otros a evolucionar de la **ejecución de detalles** a la **maestría de sistemas**. 

No se trata de aprender a usar una herramienta nueva, sino de rediseñar nuestra relación con la técnica. Es dejar de pelear con la corriente para empezar a construir los diques que le dan forma y propósito al agua.

---

### **Notas**

[^aix]: **AIX (AI Experience):** La práctica de diseñar el entorno de desarrollo (archivos de configuración, documentación, reglas) asumiendo que el usuario principal es un agente de IA. Un buen AIX reduce drásticamente las alucinaciones al darle a la máquina "barandas" claras.

[^incitaciones]: **Incitaciones:** Mi colección personal de protocolos de reconocimiento y estructuras de pensamiento en [GitHub](https://github.com/charly-vibes/incitaciones).

[^wai]: **WAI:** Un orquestador de conocimiento y herramientas diseñado para capturar el research, las decisiones y las mejores prácticas, garantizando que la infraestructura de desarrollo mantenga la calidad en cada artefacto producido. Podés ver el proyecto en [GitHub](https://github.com/charly-vibes/wai).

[^openspec]: **OpenSpec:** Un estándar abierto para definir qué debe hacer un programa de manera que sea legible para modelos de lenguaje, facilitando la autonomía de la IA sin perder la trazabilidad.

[^resonant-coding]: **Resonant Coding:** Un método para dominar el caos de la IA adecuando el proceso para encontrar la frecuencia en la cual el equipo vibra. Podés leer más en [mi post anterior](/2026/01/25/resonant-coding.html).

[^rule5]: **Regla de los 5:** Un proceso iterativo de refinamiento (Borrador, Corregir, Claridad, Casos Límite, Excelencia) que asegura la calidad de cada paso.

[^incitaciones-review]: **Incitaciones de Review:** Protocolos de auditoría especializados (seguridad, arquitectura, legibilidad) que forman parte de mi colección de **prompts y metaprompts** en [GitHub](https://github.com/charly-vibes/incitaciones).

[^beads]: **Beads:** Unidades atómicas de trabajo que representan un cambio mínimo e independiente. Al encadenarlos, forman la historia completa de la implementación. Concepto basado en el trabajo de [Steve Yegge](https://github.com/steveyegge/beads).
