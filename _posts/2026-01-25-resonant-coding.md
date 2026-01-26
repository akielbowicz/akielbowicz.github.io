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

Frustrado por el estancamiento, empecé a buscar referentes que hubieran enfrentado problemas similares. Así llegué a las ideas de Steve Yegge y Dex Horthy[^context-eng], que me dieron un marco para empezar a construir una solución. Esta es la síntesis que aplicamos en mi equipo para aterrizar esos conceptos.

Curiosamente, el problema pareció resolverse solo por un momento. A finales de octubre, la calidad del trabajo que entregaba el equipo mejoró drásticamente. Al principio pensé que habíamos logrado algo, pero la razón era otra: una de las herramientas de programación con IA que usábamos había recibido una actualización importante. Esto reforzó mi convicción: no podíamos depender solo de las mejoras de la herramienta, necesitábamos un proceso de trabajo propio y robusto. Coincidentemente, por esa misma fecha salió el libro *Vibe Coding*, que validó muchas de las ideas que ya venía madurando y que habíamos empezado a probar con el equipo.

Para que nuestro proceso no dependa del azar de una actualización técnica, debemos dejar de ver a la IA como una caja negra mágica y entender cómo opera realmente su 'motor'. Solo conociendo sus límites podemos diseñar un método que los compense.

### Entendiendo a la bestia: cómo "piensa" una IA

La idea principal de este enfoque es tener un proceso estructurado para usar la IA, que sea flexible y simple. Para eso, primero hay que entender cómo funcionan estos modelos de lenguaje (MdL)[^mdl].

Podemos entender su funcionamiento bajo cuatro premisas clave:
- Son **predictores de texto**, como el autocompletado del celular, pero inmensamente más avanzados.
- **No tienen memoria**. No recuerdan conversaciones pasadas, solo ven el texto que les presentamos en un momento dado[^memoria].
- Su **atención es limitada**. Cuanto más largo es el texto que les damos, menos eficientes se vuelden.
- **No son predecibles**. Para la misma pregunta, pueden dar respuestas distintas.

Para entender el poder y la limitación de su atención, hagamos un ejercicio. Imagina que en un almuerzo preguntas: "¿Qué puedo cocinar?". Las respuestas posibles son casi infinitas.

Ahora, añade detalles: "¿Qué comida fácil puedo hacer para seis amigos un domingo, si tengo pollo, papas y tomates?". La pregunta acotada guía a tus amigos hacia una respuesta útil. Con las IA pasa lo mismo: la calidad de la respuesta depende de la calidad de las instrucciones que les damos.

El problema es que su atención limitada se "ensucia". Pensemos en una analogía: su atención es como un balde de agua limpia que usamos para lavar platos en un río.
- Con un plato, un balde es más que suficiente.
- Con diez platos, el agua empieza a enturbiarse.
- Con cien platos, el agua está tan sucia que los últimos platos quedan peor que antes.
- Peor aún, si echamos grasa al balde —el equivalente al "ruido" en los prompts, como información irrelevante o instrucciones contradictorias—, el agua se vuelve inservible de inmediato.

Para aprovechar la atención limitada de las IA, debemos ser cuidadosos con la información que les damos y dividir los problemas grandes en partes más pequeñas, usando un "balde de agua limpia" para cada una. Cuando logramos que la información que le damos (la 'frecuencia' de nuestro mensaje) coincide con su capacidad de atención, el sistema 'resuena' y la calidad de la respuesta mejora drásticamente.

### La herramienta universal: La Regla de los 5

Para asegurar la calidad en cada paso, nos apoyamos en lo que Steve Yegge define como la **"Regla de los 5"**[^rule5], un filtro de calidad que adaptamos de la siguiente manera:

1.  **Borrador:** Crear el contenido inicial, buscando que sea completo antes que perfecto.
2.  **Corrección:** ¿La información es correcta? Se corrigen errores e inconsistencias.
3.  **Claridad:** ¿Se entiende con facilidad? Se simplifica el lenguaje y se explica todo claramente.
4.  **Casos Límite:** ¿Qué podría salir mal? Se consideran escenarios poco comunes.
5.  **Excelencia:** ¿Es lo mejor que podemos hacer? Se busca optimizar o mejorar el resultado.

Este ciclo de revisión se aplica a cada una de las fases siguientes hasta que el resultado sea sólido.

### El método: Investigación, Planificación e Implementación

Implementamos una metodología en tres fases para manejar este flujo de trabajo.

#### 1. Investigación

Dada una tarea, el primer paso es usar la IA para que investigue. Le pedimos que nos diga qué partes del programa son importantes, cómo se conectan entre sí y si hay documentación útil. Con esa información, le pedimos que cree un resumen. Este resumen es nuestro primer "balde de agua", cuidadosamente llenado.

Una vez que tenemos el borrador, lo sometemos a la "Regla de los 5" hasta que la investigación sea sólida.

#### 2. Planificación

Con la investigación ya revisada, iniciamos una nueva conversación (un nuevo "balde de agua limpia"). Le entregamos el resumen y le pedimos que genere un plan de acción detallado.

Crucialmente, cada tarea del plan debe ser lo suficientemente pequeña para ser realizada en un solo paso. Para asegurar esto, dividimos el plan en subtareas y describimos cada una con la información necesaria. Luego, aplicamos la "Regla de los 5" a cada una de estas subtareas.

#### 3. Implementación

Con las tareas bien definidas, la fase de "escritura" de las instrucciones se vuelve muy predecible. La IA ejecuta cada pequeña tarea de forma independiente. Su facilidad para esto es enorme: puede modificar decenas de archivos o crear pruebas de validación en segundos, algo que a una persona le llevaría horas.

Finalmente, una vez terminado todo, volvemos a aplicar la "Regla de los 5" al conjunto completo para asegurar que todo esté bien integrado. Este enfoque de detectar errores lo antes posible es algo en lo que las IA son extremadamente eficientes[^shift].

### De la tarea a la plantilla

Este flujo no solo nos entrega un programa funcionando; nos deja como 'subproducto' una serie de instrucciones y criterios que ya han sido filtrados por la Regla de los 5. Es aquí donde el método se vuelve escalar: estas piezas de conocimiento se convierten en plantillas reutilizables para cualquier otro desafío, desde la medicina hasta la organización de eventos.

Podemos aplicar el mismo método para generar los materiales que nos guían en cada paso, como "prompts" o plantillas específicas para un tipo de problema. Por ejemplo, Charly utiliza esta idea para crear distintas "visiones" de cómo implementar código, definiendo sus preferencias y estilo. Esto nos permite aprovechar metodologías ya estudiadas en otras profesiones (desde la cirugía a la organización de un mundial) para que la IA nos ayude a aplicarlas en nuestros propios procesos.

### Guía de inicio rápido: Cómo aplicar Resonant Coding hoy

Para que este artículo pase de ser un ensayo a una guía accionable, aquí tienes una bajada a tierra para que sepas qué hacer la próxima vez que uses una IA para una tarea compleja.

#### 1. Elige tu Conversación (El Protocolo)

Imagina que tienes tres expertos en una sala. No le hablarías a los tres a la vez del mismo tema de forma desordenada. Asigna una tarea a cada uno:

*   **El Investigador (Conversación 1):** Tu objetivo es entender.
    *   **Petición:** "Actúa como un experto en [tema]. Quiero entender [situación]. Explícame los conceptos clave y resúmelos en 3 puntos."
    *   **Tu Trabajo:** Revisa el resumen. Si es necesario aplicar la "Regla de los 5" para refinarlo, **inicia una nueva conversación**, pega el resumen y pídele a la IA que lo mejore según la regla. Itera hasta que el resumen sea sólido.

*   **El Estratega (Conversación 2):** Tu objetivo es planificar.
    *   **Acción:** Inicia una nueva conversación ("limpia el balde").
    *   **Petición:** "Basado en este resumen [pega el resumen del Investigador], crea un plan paso a paso para lograr [tu objetivo]."
    *   **Tu Trabajo:** Revisa el plan. Si es necesario aplicar la "Regla de los 5" para refinarlo, **inicia una nueva conversación**, pega el plan y pídele a la IA que lo mejore según la regla. Pide los ajustes necesarios hasta que cada paso sea claro, atómico (es decir, que no se pueda dividir en tareas más pequeñas) y robusto.

*   **El Ejecutor (Conversaciones 3+):** Tu objetivo es actuar.
    *   **Acción:** Por cada paso del plan, **inicia una nueva conversación**.
    *   **Petición:** "Vamos a ejecutar este paso: [pega el paso del plan]."
    *   **Tu Trabajo:** Verifica el resultado. Si es necesario aplicar la "Regla de los 5" para refinarlo, **inicia una nueva conversación**, pega el resultado y pídele a la IA que lo mejore según la regla.

#### 2. La Razón del "Balde Limpio": Gestionando el Contexto

Cada vez que **inicias una nueva conversación**, te aseguras de que la IA solo vea la información más relevante y refinada. Esto es crucial porque la "atención" de la IA es un recurso limitado. En conversaciones largas, el contexto se llena de borradores, correcciones y dudas, lo que "ensucia el agua" y reduce la calidad de las respuestas.

Para facilitar el "copiar y pegar" entre conversaciones, puedes pedirle a la IA que resuma el resultado final en un formato limpio.

**Ejemplo de Petición al final de una fase:**
> "Excelente. Ahora, resume nuestro plan final en un único bloque de texto plano, sin comentarios adicionales, para que pueda copiarlo fácilmente."

#### 3. El Arte de Preguntar

La calidad de la respuesta depende de la calidad de la pregunta. No es lo mismo pedir "ideas para vacaciones" que dar detalles que guíen a la IA.

**Petición Vaga:**
> "Ayúdame a planear un evento."

**Petición Clara:**
> "Actúa como un organizador de eventos profesional. Necesito planificar un evento de recaudación de fondos para un refugio de animales local. El objetivo es recaudar $5,000 y aumentar la conciencia sobre la adopción. El evento será en un parque local en tres meses y esperamos 100-150 asistentes. Dame un plan detallado que incluya: una lista de posibles actividades (ej. concurso de disfraces de mascotas, puesto de adopción), un cronograma de planificación desde ahora hasta el evento, y sugerencias para promocionar el evento en redes sociales. El tono debe ser entusiasta y centrado en la comunidad."

#### 4. Sé el Director, no el Espectador

Tu rol es dirigir a la IA. Antes de aceptar una respuesta, usa la "Regla de los 5" como un filtro mental:

*   **¿Es correcto?** ¿La información tiene sentido?
*   **¿Es claro?** ¿Lo entiendo a la primera?
*   **¿Considera alternativas?** ¿Qué podría salir mal?
*   **¿Es excelente?** ¿O solo "aceptable"?

Si no cumple tus expectativas, pide una mejora.

#### 5. Define tu Estilo

Si tienes preferencias sobre el estilo de comunicación, guárdalas. Al inicio de una conversación, puedes pedirle a la IA que las adopte.

*   **Ejemplo:** "En todas tus respuestas, utiliza un tono formal y académico. Cita tus fuentes cuando sea posible y estructura la información en listas."

### Conclusión: Encontrar la resonancia

Una instrucción mal dada puede generar cientos de líneas de código erróneo. Un plan mal definido, decenas de miles. Por eso, este proceso estructurado es vital. Los resultados de cada paso deben ser revisados por personas. Las IA son buenas, pero el conocimiento que solo existe en la cabeza del equipo aún debe ser aportado por nosotros.

Este enfoque nos permite generar un trabajo de mucha más calidad de lo que podría hacer por mi cuenta, y en una fracción del tiempo[^future-work].

Elegí el nombre "Resonant Coding" para bautizar esta síntesis de influencias porque me recuerda a la "Estación de Ondas"[^ondas] que vi en la facultad. Si agitas una soga a una frecuencia específica, el caos de movimiento se transforma en estructuras fijas y armónicas. Con este método hacemos algo similar: adecuamos el proceso para encontrar la frecuencia correcta en la cual nuestro sistema "vibra". dejamos de generar ruido y empezamos a crear con resonancia[^phorma].

---
### Notas

[^mdl]: **MdL (Modelo de Lenguaje Grande)**: Un tipo de programa de inteligencia artificial entrenado para entender y generar texto de manera similar a un humano.

[^charly]: Se puede encontrar el post original de Charly en [Resonant Coding](https://charly-vibes.github.io/microdancing/es/posts/resonant-coding).

[^memoria]: Algunas herramientas simulan tener **memoria**, pero lo que hacen es agregar información de la conversación pasada a la conversación actual para mantener el hilo.

[^context-eng]: Las ideas de "Context Engineering" de Dex Horthy se pueden explorar en este documento sobre [Advanced Context Engineering for Coding Agents](https://github.com/humanlayer/advanced-context-engineering-for-coding-agents/blob/main/ace-fca.md).

[^rule5]: La "Regla de los 5" es un concepto detallado por Steve Yegge. Puede leerse más en su [documentación original](https://github.com/steveyegge/gastown/blob/main/internal/formula/formulas/rule-of-five.formula.toml).

[^shift]: En la industria del software, a esta práctica de adelantar la detección de errores se la conoce como "shift-left".

[^ondas]: La **Estación de Ondas** es un experimento de física que muestra el fenómeno de la resonancia. Se puede ver una [demostración en video](https://www.youtube.com/watch?v=6zBknO95rB4) de una de las exhibiciones de la Semana de la Física en la UBA.

[^fridai]: Las **fridAI** son reuniones quincenales de una hora que se realizan en el equipo para discutir y compartir prácticas y el uso de la Inteligencia Artificial en el trabajo.

[^future-work]: Las implicaciones de estos cambios son profundas. En un futuro post, planeo explorar qué habilidades necesitaremos para adaptarnos a la nueva estructura global del trabajo, así como una visión crítica sobre quiénes tendrán acceso a estas herramientas y la disparidad que esto podría generar.

[^phorma]: Llevo estas mismas metodologías a la investigación científica y la industria a través de mi emprendimiento [phorma scientific](por-que-arme-phorma).

---