# Resonant Coding: Cómo Dejar de Programar y Empezar a Construir con IA

## Introducción: La Paradoja del Creador

Algo con lo que siempre menciono es el tema de que no me gusta escribir codigo, no me gusta tener que programar porque es una tarea tediosa y complicada, dificil de hacer y muy facil hacerlo mal. Requiere tener una vision general de lo que vamos a hacer y anticiparnos a muchos problemas. Pero a la vez me gusta crear cosas, me gusta entender las ideas y me gusta probar cosas nuevas.

El problema es que a menudo nos encontramos en una situación que describí en una charla reciente:

> ...estamos dándonos cuenta de que si nos subimos a un caballo podemos llegar más lejos, más rápido y sin cansarnos. El único problema es que estamos en la etapa de que todavía no sabemos que necesitamos la montura, entonces no llegamos muy lejos y llegamos hechos pelota.

Esto que estoy por contar es la búsqueda de esa "montura". Es una metodología que he llamado **Resonant Coding**. No se trata de "live coding", sino de un proceso de ingeniería estructurado para extraer la máxima energía de nuestro "caballo" (la IA) y aprovecharla al máximo.

## El Fundamento: Entendiendo a Nuestro "Genio de la Lámpara" (Context Engineering)

Para poder entender porque esto funciona tenemos que pensar en las ideas de lo que tenemos en una sola vision. Que es el Context Engineering que lo presento Dex Horthly. Dentro del context engineering lo que tenemos que entender es que un modelo de lenguaje funciona como una operación sin estado que construye respuestas de manera probabilística.

Entendiendo que el contexto es limitado y que lo que devuelve es cada vez mas impreciso, tenemos que pensar que las palabras que vienen de más lejos son menos eficientes. La idea es poder aprovechar al máximo la primera parte del contexto de manera que la respuesta que tengamos sea lo mejor posible, dándole tareas que cada vez tienen que ser mas pequeñas.

### Un Ejemplo Práctico: La Contaminación del Contexto
Un error común es llenar el contexto de la IA con herramientas e información irrelevante. Un caso concreto surgió al instalar un kit de desarrollo nuevo:

> ...el otro día que instalé el SDK de el kit del Spectri Development, me los instaló en el ambiente global y también hay un problema de tener tantos MCPs prendidos al, no sé, divino botón porque te gasta contexto. Cada cada uno de estos te agrega definiciones de herramientas en el contexto [...] es como que estás tirando plata. [...] No me gustó mucho del de ese kit que te lo instalas y te instala de manera global. Entonces está por todos lados y tenés que empezar a hacer maniobras para que no te funcionen en distintos repositorios.

### Filosofía de Herramientas: ¿MCP o Script?
Esto nos lleva a pensar cuándo usar herramientas complejas como los MCPs (Mercado Libre Custom Prompts). No son una solución para todo:

> Para mí es como que también nos volvemos un poco bajos y decimos, "Bueno, creo un MCP, pero si sabes que tiene que ser algo determinístico, ¿por qué vas a crear algo particular?"

La regla general que veo es que un MCP es ideal para interactuar con sistemas externos sobre los que no tenemos control directo:

> El MCP está bueno para acceder cosas, para acceder a datos o acceder a sistemas sobre los cuales uno no podría tener control. Por ejemplo, te queres conectar a Jira, bueno, te conectas a través del del MCP o te conectas a Big Query a través de un MCP.

Y cuando lo usamos, debe ser más que una simple API. Debe ser una herramienta para agentes:

> El MCP sí, si lo queremos hacer para algo agéntico, sí es como, "Che, llamaste esto, bueno, te dio tal resultado, quizás te conviene llamar a estos otros o podés actualizar tal otra cosa." Entonces, no pensarlo como que sean solo APIs, sino verlo como darle realmente cambiarle el contexto porque si no, es una API cara.

## La Metodología en 3 Pasos: Research, Plan, Implement

Aplicamos una metodologia de Research-Plan-And-Implement. Tomemos por caso que queremos modificar algo, agregar un feature, o arreglar un problema.

### Paso 1: Investigación (Research)
Le pedimos al modelo que nos investige todo lo relacionado al problema. En este punto, las cosas que describe tienen que ser tal cual son, no tiene que inventar nada. Es un paso de recolección de hechos. Las herramientas actuales, como Cursor, ya nos brindan capacidades avanzadas para esto. Una vez investigado, aplicamos la 'Regla de los 5' para asegurar la completitud y precisión de la información.

### Paso 2: Planificación (Plan)
Una vez que ya tenemos la investigación completa, definimos el plan. Con instrucciones claras, le pedimos que estructure un plan detallado paso a paso, considerando los cambios necesarios y los puntos clave a tener en cuenta. Aquí es donde podemos aplicar directivas como 'aplica TDD', 'toma las tareas de una en una', o 'evita implementar todo junto', asegurando que el plan sea crítico y con definiciones claras.

### Paso 3: Implementación (Implement)
Ejecutamos el plan. Si la tarea es lo suficientemente pequeña, podemos delegar directamente su implementación y revisar que el comportamiento sea el esperado. Para tareas más grandes, divido el proceso en tickets pequeños (yo uso `beads` localmente), manteniendo el contexto de la IA acotado en cada paso. Es crucial validar cada implementación con tests unitarios generados a partir de la investigación inicial.

## Conclusión: De Artesano a Ingeniero de Sistemas

Esto ya es un proceso de ingenieria en el sentido de tener que realizar algo con los menores recursos y de la mejor manera.

> En algún chat, alguna vez leí que un profesor decía: 'Cualquiera puede construir un puente, pero solo los expertos lo pueden hacer con el menor esfuerzo, optimizando el uso de los recursos y el mejor proceso'.

Esa es la analogía que tenemos que empezar a ver. Con esto, pasaremos de la construcción manual a usar herramientas que nos permiten 'levantar edificios en semanas'. Para lograrlo, la clave es una planificación minuciosa, coordinación efectiva y una visión global clara de lo que se está construyendo.

---
## Referencias

*   **Context Engineering (Dex Horthly):** 
*   **pudding.cool:** 
*   **Regla de los 5 (Rule of 5):** 
*   **Test-Driven Development (TDD):** 
*   **Beads (Herramienta de ticketing):** 
