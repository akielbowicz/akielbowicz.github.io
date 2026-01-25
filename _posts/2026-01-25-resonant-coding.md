---
layout: default
title: "Resonant Coding: un método para dominar el caos de la IA"
lang: es
---
# Resonant Coding: un método para dominar el caos de la IA

*This post is also available in [English](/2026/01/25/resonant-coding-en.html).*

*Este artículo adapta ideas del post sobre Resonant Coding de Charly[^charly] y es una adaptación de lo presentado en las fridAI la semana pasada[^fridai], pero no asume conocimiento técnico previo.*

### El problema: una avalancha de instrucciones

Como líder de un equipo de desarrollo en Mercado Libre, me enfrenté a un desafío particular. Estábamos creando un proyecto desde cero, pero el equipo tenía pocos programadores con mucha experiencia, lo que exigía que yo revisara gran parte del trabajo. Al mismo tiempo, la empresa nos impulsaba a usar Inteligencia Artificial (IA) para ir más rápido.

El resultado fue una paradoja. Nos vimos inundados por una cantidad abrumadora de "código" —las instrucciones que forman los programas— generado por estas IA. Estas instrucciones eran a menudo complicadas de entender, y no siempre tenían la calidad necesaria. El proceso de revisión se llenó de idas y vueltas, volviéndose lento y frustrante. En lugar de acelerar, nos habíamos estancado.

La solución a este caos la empecé a destilar a principios de año, durante unas vacaciones, a partir de las ideas de dos expertos en la materia: Steve Yegge y Dex Horthly[^context-eng]. De ahí nació el núcleo de este método.

Curiosamente, el problema pareció resolverse solo por un momento. A finales de octubre, la calidad del trabajo que entregaba el equipo mejoró drásticamente. Al principio pensé que habíamos logrado algo, pero la razón era otra: una de las herramientas de programación con IA que usábamos había recibido una actualización importante. Esto reforzó mi convicción: no podíamos depender solo de las mejoras de la herramienta, necesitábamos un proceso de trabajo propio y robusto. Coincidentemente, por esa misma fecha salió el libro *Vibe Coding*, que validó muchas de las ideas que ya venía madurando.

### Entendiendo a la bestia: cómo "piensa" una IA

La idea principal de mi método es tener un proceso estructurado para usar la IA, que sea flexible y simple. Para eso, primero hay que entender cómo funcionan estos modelos de lenguaje (MdL)[^mdl].

Yo los resumo así:
- Son **predictores de texto**, como el autocompletado del celular, pero inmensamente más avanzados.
- **No tienen memoria**. No recuerdan conversaciones pasadas, solo ven el texto que les presentamos en un momento dado[^memoria].
- Su **atención es limitada**. Cuanto más largo es el texto que les damos, menos eficientes se vuelden.
- **No son predecibles**. Para la misma pregunta, pueden dar respuestas distintas.

Para entender el poder y la limitación de su atención, hagamos un ejercicio. Imagina que en un almuerzo preguntas: "¿Qué puedo cocinar?". Las respuestas posibles son casi infinitas.

Ahora, añade detalles: "¿Qué comida fácil puedo hacer para seis amigos un domingo, si tengo pollo, papas y tomates?". La pregunta acotada guía a tus amigos hacia una respuesta útil. Con las IA pasa lo mismo: la calidad de la respuesta depende de la calidad de las instrucciones que les damos.

El problema es que su atención limitada se "ensucia". Pensemos en una analogía: estamos de camping y tenemos que lavar los platos en el río con un solo balde de agua.
- Para un plato, un balde sobra.
- Para 10 platos, el agua empieza a enturbiarse.
- Para 100 platos, un balde no alcanza y el agua termina tan sucia que los últimos platos quedan igual o peor.
- Peor aún, si echamos grasa al balde (información irrelevante), el agua queda inutilizable.

Para aprovechar la atención limitada de las IA, debemos ser cuidadosos con la información que les damos y dividir los problemas grandes en partes más pequeñas, usando un "balde de agua limpia" para cada una.

### El método: Investigación, Planificación e Implementación

Para manejar este flujo de trabajo, propongo una metodología en tres fases.

#### 1. Investigación

Dada una tarea, el primer paso es usar la IA para que investigue. Le pedimos que nos diga qué partes del programa son importantes, cómo se conectan entre sí y si hay documentación útil. Con esa información, le pedimos que cree un resumen. Este resumen es nuestro primer "balde de agua", cuidadosamente llenado.

Pero no nos detenemos ahí. Sometemos este resumen a un proceso de revisión crítica que llamo la **"Regla de los 5"**[^rule5]:

1.  **Borrador:** Crear el contenido inicial, buscando que sea completo antes que perfecto.
2.  **Correctitud:** ¿La información es correcta? Se corrigen errores e inconsistencias.
3.  **Claridad:** ¿Se entiende con facilidad? Se simplifica el lenguaje y se explica todo claramente.
4.  **Casos Límite:** ¿Qué podría salir mal? Se consideran escenarios poco comunes.
5.  **Excelencia:** ¿Es lo mejor que podemos hacer? Se busca optimizar o mejorar el resultado.

Este ciclo se repite hasta que el resumen de la investigación sea sólido.

#### 2. Planificación

Con la investigación ya revisada, iniciamos una nueva conversación (un nuevo "balde de agua limpia"). Le entregamos el resumen y le pedimos que genere un plan de acción detallado.

Crucialmente, cada tarea del plan debe ser lo suficientemente pequeña para ser realizada en un solo paso. Para asegurar esto, dividimos el plan en subtareas y describimos cada una con la información necesaria. Luego, aplico la "Regla de los 5" a cada una de estas subtareas.

#### 3. Implementación

Con las tareas bien definidas, la fase de "escritura" de las instrucciones se vuelve muy predecible. La IA ejecuta cada pequeña tarea de forma independiente. Su facilidad para esto es enorme: puede modificar decenas de archivos o crear pruebas de validación en segundos, algo que a una persona le llevaría horas.

Finalmente, una vez terminado todo, volvemos a aplicar la "Regla de los 5" al conjunto completo para asegurar que todo esté bien integrado. Este enfoque de detectar errores lo antes posible es algo en lo que las IA son extremadamente eficientes[^shift].

### Reutilizando la metodología

Lo bueno de este proceso es que es reutilizable. Podemos aplicar el mismo método para generar los materiales que nos guían en cada paso, como "prompts" o plantillas específicas para un tipo de problema. Por ejemplo, Charly utiliza esta idea para crear distintas "visiones" de cómo implementar código, definiendo sus preferencias y estilo. Esto nos permite aprovechar metodologías ya estudiadas en otras profesiones (desde la cirugía a la organización de un mundial) para que la IA nos ayude a aplicarlas en nuestros propios procesos.

### Conclusión: Encontrar la resonancia

Una instrucción mal dada puede generar cientos de líneas de código erróneo. Un plan mal definido, decenas de miles. Por eso, este proceso estructurado es vital. Los resultados de cada paso deben ser revisados por personas. Las IA son buenas, pero el conocimiento que solo existe en la cabeza del equipo aún debe ser aportado por nosotros.

Este método me permite generar un trabajo de mucha más calidad de lo que podría hacer por mi cuenta, y en una fracción del tiempo[^future-work].

El nombre "Resonant Coding" me recuerda a la "Estación de Ondas"[^ondas] que vi en la facultad. Si agitas una soga a una frecuencia específica, el caos de movimiento se transforma en estructuras fijas y armónicas. Con este método hacemos algo similar: adecuamos el proceso para encontrar la frecuencia correcta en la cual nuestro sistema "vibra". dejamos de generar ruido y empezamos a crear con resonancia[^phorma].

---
### Notas

[^mdl]: **MdL (Modelo de Lenguaje Grande)**: Un tipo de programa de inteligencia artificial entrenado para entender y generar texto de manera similar a un humano.

[^charly]: Se puede encontrar el post original de Charly en [Resonant Coding](https://charly-vibes.github.io/microdancing/resonant-coding).

[^memoria]: Algunas herramientas simulan tener **memoria**, pero lo que hacen es agregar información de la conversación pasada a la conversación actual para mantener el hilo.

[^context-eng]: Las ideas de "Context Engineering" de Dex Horthly se pueden explorar en este documento sobre [Advanced Context Engineering for Coding Agents](https://github.com/humanlayer/advanced-context-engineering-for-coding-agents/blob/main/ace-fca.md).

[^rule5]: La "Regla de los 5" es un concepto detallado por Steve Yegge. Puede leerse más en su [documentación original](https://github.com/steveyegge/gastown/blob/main/internal/formula/formulas/rule-of-five.formula.toml).

[^shift]: En la industria del software, a esta práctica de adelantar la detección de errores se la conoce como "shift-left".

[^ondas]: La **Estación de Ondas** es un experimento de física que muestra el fenómeno de la resonancia. Se puede ver una [demostración en video](https://www.youtube.com/watch?v=6zBknO95rB4) de una de las exhibiciones de la Semana de la Física en la UBA.

[^fridai]: Las **fridAI** son reuniones quincenales de una hora que se realizan en el equipo para discutir y compartir prácticas y el uso de la Inteligencia Artificial en el trabajo.

[^future-work]: Las implicaciones de estos cambios son profundas. En un futuro post, planeo explorar qué habilidades necesitaremos para adaptarnos a la nueva estructura global del trabajo, así como una visión crítica sobre quiénes tendrán acceso a estas herramientas y la disparidad que esto podría generar.

[^phorma]: Llevo estas mismas metodologías a la investigación científica y la industria a través de mi emprendimiento [phorma scientific](por-que-arme-phorma).

---


