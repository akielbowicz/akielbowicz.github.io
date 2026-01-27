---
layout: default
title: "Resonant Coding: un método para dominar el caos de la IA"
lang: es
---
# Resonant Coding: un método para dominar el caos de la IA

*This post is also available in [English](/2026/01/25/resonant-coding-en.html).*

*Este artículo adapta ideas del post sobre Resonant Coding de Charly[^charly] y es una adaptación de lo presentado en las fridAI la semana pasada[^fridai], pero no asume conocimiento técnico previo.*

### El problema: gente haciendo cualquiera

Desde hace unos meses estoy liderando un equipo de desarrollo en Mercado Libre, armando algo desde cero para dar soporte a Planificación Financiera. El equipo era nuevo, con poca gente experimentada, lo cual significaba que yo tenía que revisar casi todo. Y al mismo tiempo, la empresa nos empujaba a usar Inteligencia Artificial para "acelerar"[^acelerar].

El resultado fue una paradoja bastante absurda: nos vimos inundados de código generado por IA que era complicado de entender, no siempre cumplía con los requisitos mínimos de calidad, y hacía que las revisiones se convirtieran en una ida y vuelta interminable. En lugar de ir más rápido, nos habíamos trabado.

Frustrado, empecé a buscar referentes. Así llegué a las ideas de Steve Yegge y Dex Horthy[^context-eng], que me dieron un marco para empezar a armar algo. Esta es la síntesis que terminamos aplicando en el equipo.

Y acá viene lo curioso: a finales de octubre, la calidad del código que entregaban mejoró de golpe. Por un par de días pensé que habíamos logrado algo. Que el método estaba funcionando.

Después descubrí que una de las herramientas que usábamos se había actualizado.

No éramos nosotros. Era el software. Y si el software podía mejorar sin nuestra intervención, también podía empeorar. O cambiar de formas que no entendíamos. No podíamos depender de eso. Coincidentemente, por esas fechas salió el libro *[Vibe Coding](https://itrevolution.com/product/vibe-coding-book/)*, que validó muchas de las ideas que ya venía madurando.

Para que nuestro proceso no dependa del azar de una actualización, hay que dejar de ver a la IA como una caja negra mágica y entender cómo funciona realmente. Solo conociendo sus límites podemos diseñar algo que los compense.

### Entendiendo a la bestia

Antes de hablar del método, un desvío necesario. Sin entender cómo funcionan estos modelos de lenguaje (MdL)[^mdl], nada de lo que sigue va a tener sentido.

Lo que hay que saber:
- Son **predictores de texto**. Como el autocompletado del celular, pero entrenados con una cantidad de datos que es difícil de conceptualizar sin recurrir a metáforas astronómicas.
- **No tienen memoria**. Cada vez que les hablás es como si fuera la primera vez. Lo que algunas herramientas llaman "memoria" es un truco: guardan parte de la conversación y la pegan silenciosamente al principio de cada mensaje nuevo[^memoria].
- **Su atención es limitada**. Y cuanto más largo es el texto que les das, peor funcionan.
- **No son predecibles**. Para la misma pregunta pueden dar respuestas distintas.

Para entender el tema de la atención, hagamos un ejercicio. Estás en un almuerzo y preguntás: "¿Qué puedo cocinar?". Las respuestas posibles son infinitas y probablemente inútiles. Ahora preguntá: "Tengo que preparar algo para 6 amigos el domingo, que sea fácil, tengo pollo, papas y tomates". La pregunta acotada guía hacia una respuesta útil. Con las IA pasa exactamente lo mismo.

El problema es que esa atención se "ensucia". La mejor manera de pensarlo es con una analogía que me vino durante una conversación sobre camping: imaginate que te fuiste de campamento y para lavar los platos tenés que ir al río con un balde a buscar agua.

- Con un plato, el balde sobra.
- Con diez, el agua empieza a enturbiarse y hay que ser cuidadoso.
- Con cien, el agua está tan sucia que los últimos platos salen peor de lo que entraron.
- Y si en algún momento tirás algo grasoso al balde —información irrelevante, instrucciones contradictorias—, el agua queda inutilizable para todo lo que sigue.

Para aprovechar esa atención limitada, hay que ser cuidadoso con lo que le metés y dividir los problemas grandes en partes más pequeñas, usando un "balde de agua limpia" para cada una. Cuando lográs que la información que le das coincide con su capacidad de atención, el sistema "resuena" y la calidad de la respuesta mejora drásticamente.

### La Regla de los 5

Acá entra el segundo ingrediente, algo que Steve Yegge llama la **"Regla de los 5"**[^rule5]. No es tanto una regla como un proceso iterativo de refinamiento. La versión simplificada: cuando generás algo, lo pasás por cinco filtros sucesivos.

1.  **Borrador:** Crear el contenido inicial. No importa que sea perfecto, importa que esté todo. Preferir amplitud a profundidad.
2.  **Corrección:** ¿Es correcto? Arreglar errores, inconsistencias, cosas que el modelo pudo haber inventado.
3.  **Claridad:** ¿Se entiende? Simplificar, eliminar jerga, explicar todo claramente.
4.  **Casos Límite:** ¿Qué podría salir mal? ¿Hay algo inusual que no estemos considerando?
5.  **Excelencia:** ¿Es lo mejor que podemos hacer? Optimizar, pulir, mejorar.

Los cinco pasos no tienen que aplicarse siempre en ese orden ni siempre completamente. A veces un documento necesita más trabajo en claridad que en corrección. El punto es tener una estructura de revisión, no seguirla ciegamente. Este ciclo se aplica a cada fase del método.

### El método: tres movimientos

No voy a describir esto como una receta de cocina porque en la práctica es más desordenado. Pero hay tres movimientos generales que se repiten.

#### Investigación

Antes de hacer cualquier cosa, hay que entender el problema. Le pedís al modelo que investigue lo que ya existe, que identifique las partes importantes y cómo se conectan entre sí, que encuentre documentación relevante. El modelo hace esto bastante bien porque es esencialmente lectura y síntesis.

Pero —y esto es importante— el documento que genera tiene que ser revisado de manera exhaustiva. Los modelos son muy buenos, pero siempre hay cosas que se les escapan porque no existen de manera concreta en los materiales del proyecto. Son ideas o conocimiento que está implícito en la cabeza de las personas. La revisión humana es la oportunidad de hacerlo explícito.

#### Planificación

Con el documento de investigación ya revisado, iniciamos una nueva conversación (balde limpio) y generamos un plan de acción. El truco: cada tarea del plan tiene que ser lo suficientemente pequeña como para caber en un solo balde. Si una tarea es "armar todo el sistema de usuarios", es demasiado grande. Si es "agregar la verificación de contraseña en la pantalla de ingreso", estamos mejor.

Cada una de estas tareas pequeñas pasa, de nuevo, por la Regla de los 5. Un plan mal definido puede generar miles de líneas de código incorrecto, y para ese punto ya es tarde[^shift].

#### Implementación

Para este punto debería ser casi mecánica. Ya tenemos casi totalmente definido qué se va a hacer, de manera que no hay mucho lugar para que el modelo se desvíe o invente cosas nuevas. Y acá es donde brillan de verdad: no les cuesta nada modificar veinte archivos, crear pruebas de validación, reorganizar estructuras completas. Lo que a una persona le llevaría horas, para ellos es cuestión de segundos.

Al final, volvemos a aplicar la Regla de los 5 al conjunto completo.

### De la tarea a la plantilla

Lo bueno de este proceso es que es reutilizable. No solo te entrega un programa funcionando; te deja como subproducto una serie de instrucciones y criterios que ya fueron filtrados por la Regla de los 5. Estas piezas de conocimiento se convierten en plantillas reutilizables.

Por ejemplo, Charly aprovechó herramientas de investigación profunda para estudiar metodologías y protocolos de otras profesiones —lanzar un cohete, hacer una cirugía, organizar un mundial— y ahora puede aplicarlas en sus propios procesos. Son procedimientos que ya están recontra estudiados y ahora podemos aprovecharlos.

### Guía de inicio rápido

Para que esto pase de ensayo a algo accionable, acá va la bajada a tierra.

#### Los tres expertos

Imaginate que tenés tres expertos en una sala. No les hablarías a los tres a la vez del mismo tema. Asignales una tarea a cada uno:

**El Investigador (Conversación 1):** Tu objetivo es entender. Pedile que actúe como experto en el tema, que te explique los conceptos clave y los resuma. Después revisá el resumen con la Regla de los 5. Si necesita mejoras, *iniciá una nueva conversación*, pegá el resumen y pedile que lo refine.

**La Estratega (Conversación 2):** Tu objetivo es planificar. Balde limpio. Pegá el resumen del investigador y pedí un plan paso a paso. Revisalo. Cada paso tiene que ser lo más pequeño posible, que no se pueda dividir más.

**El Ejecutor (Conversaciones 3+):** Por cada paso del plan, nueva conversación. Ejecutá, verificá el resultado, refiná si hace falta.

#### Por qué tantas conversaciones

Cada vez que iniciás una conversación nueva, te asegurás de que la IA solo vea información relevante y refinada. En conversaciones largas, el contexto se llena de borradores, correcciones y dudas, y eso ensucia el agua.

Un tip: al final de cada fase, pedile que resuma el resultado en un bloque limpio para poder copiarlo fácil.

#### El arte de preguntar

La calidad de la respuesta depende de la calidad de la pregunta.

**Petición vaga:** "Ayúdame a planear un evento."

**Petición clara:** "Necesito planificar un evento de recaudación de fondos para un refugio de animales. El objetivo es recaudar $5,000. El evento será en un parque en tres meses, esperamos 100-150 personas. Dame un plan que incluya: actividades posibles (concurso de disfraces, puesto de adopción), cronograma de planificación, y cómo promocionarlo en redes. El tono tiene que ser entusiasta y centrado en la comunidad."

#### Sé el director, no el espectador

Tu rol es dirigir. Antes de aceptar una respuesta, filtrala:
- ¿Es correcto?
- ¿Se entiende a la primera?
- ¿Qué podría salir mal?
- ¿Es lo mejor que puede ser, o solo "aceptable"?

Si no cumple, pedí una mejora. Y si tenés preferencias de estilo, guardalas y pasalas al inicio de cada conversación.

### Encontrar la resonancia

Una instrucción mal dada puede generar cientos de líneas de código incorrecto. Un plan mal definido, decenas de miles. Por eso este proceso es vital. Los resultados de cada paso tienen que ser revisados por personas. Los modelos son muy buenos, pero el conocimiento que solo existe en la cabeza del equipo —implícito, no escrito en ningún lado— todavía tiene que ser aportado por nosotros.

Hay algo que me molesta de la narrativa dominante sobre la IA: la idea de que te permite "ir más rápido". No es falso exactamente, pero es engañoso. Si lo que hacemos es mandar todo de una, vamos a seguir quemando árboles por el gusto de ver cómo se quema un árbol[^energia].

Este método no es un atajo. Toma más tiempo que tirarle una instrucción al modelo y esperar que salga algo bueno. Pero ese tiempo se recupera multiplicado porque los errores se detectan temprano, el trabajo no tiene que rehacerse, y cuando algo se termina ya se sabe que está bien[^future-work].

La idea de llevar un proceso a algo más estructurado me retrae a la Estación de Ondas[^ondas] en el playón del pabellón 2 de la facultad durante la Semana de la Física. Alguien agarra una soga y la empieza a agitar. Al principio es puro caos, ondas que chocan entre sí. Pero si encontrás la frecuencia correcta, algo pasa: el caos se ordena. Aparecen puntos que no se mueven y puntos que oscilan al máximo. Estructuras que se sostienen solas porque el sistema entró en resonancia.

Con este método hacemos algo similar: adecuamos el proceso para encontrar la frecuencia en la cual el equipo vibra[^phorma].

---
### Notas

[^acelerar]: "Acelerar" es una de esas palabras que en contextos corporativos significa simultáneamente todo y nada. Puede significar "producir más" o "gastar menos" o "adoptar la tecnología de moda" o alguna combinación de las anteriores.

[^mdl]: **MdL (Modelo de Lenguaje Grande)**: Un tipo de programa de inteligencia artificial entrenado para entender y generar texto de manera similar a un humano. Esencialmente, predictores de texto probabilísticos muy avanzados.

[^charly]: El post original de Charly en [Resonant Coding](https://charly-vibes.github.io/microdancing/es/posts/resonant-coding) tiene más detalles técnicos y ejemplos concretos.

[^memoria]: Lo que algunas herramientas llaman "memoria" es en realidad un truco: guardan parte de la conversación anterior y la agregan al mensaje nuevo. Tiene límites, y cuando se superan hay que recortar. Algo siempre se pierde.

[^context-eng]: Las ideas de "Context Engineering" de Dex Horthy se pueden explorar en este [documento técnico](https://github.com/humanlayer/advanced-context-engineering-for-coding-agents/blob/main/ace-fca.md). Es denso pero vale la pena.

[^rule5]: La Regla de los 5 de Steve Yegge está en su [documentación original](https://github.com/steveyegge/gastown/blob/main/internal/formula/formulas/rule-of-five.formula.toml).

[^shift]: A la práctica de detectar errores lo antes posible se la conoce como "shift-left". La idea es que cuanto antes encontrás un problema, más barato es arreglarlo.

[^ondas]: La Estación de Ondas es un experimento de física que muestra el fenómeno de la resonancia. Se puede ver una [demostración en video](https://www.youtube.com/watch?v=6zBknO95rB4) de la Semana de la Física de la UBA.

[^fridai]: Las **fridAI** son reuniones quincenales de una hora que hacemos en el equipo para compartir prácticas sobre el uso de IA en el trabajo.

[^future-work]: Las implicaciones de estos cambios son profundas. En un futuro post quiero explorar qué habilidades vamos a necesitar para adaptarnos, y también una visión más crítica sobre quiénes van a tener acceso a estas herramientas y la disparidad que eso puede generar.

[^energia]: No es solo una metáfora. Cada consulta a un modelo de lenguaje consume energía y recursos. Usarlos sin criterio tiene un costo real.

[^phorma]: Llevo estas mismas metodologías a la investigación científica y la industria a través de mi emprendimiento [phorma scientific](https://phorma.sh/).

---