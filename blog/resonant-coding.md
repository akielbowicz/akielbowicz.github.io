# intro

este articulo es una adaptacion más general del post de Charly sobre Resonant Coding y no asume ningún conocimiento técnico previo, para ver el workflow completo y ejemplos técnicos pueden ver el post de Charly. 

- mercadolibre exigiendo que trabajes mas usando IA 
- gente haciendo cualquiera mandando cantidades inhumanas de codigo
- como hacemos para revisar todo eso, se vuelve un deadlock

Durante los últimos meses en los que estuve trabajando en Mercado Libre como Lider Técnico armando un equipo nuevo
para dar soporte a los equipos de Planificación Financiera 

- Tener accesso a muchos Tokens
- Tener problemas nuevos para resolver "green-field" y construir algo completamente nuevo
- El equipo era nuevo con pocos desarrolladores Senior (que tienen independencia y a los cuales se puede delegar) y requería mucha revisión por parte de mí parte.
- Una incitacion constante a utilizar cada vez mas la IA para ver si realmente podemos acelerar el proceso

- Los problemas que surgian:
    - Mucha cantidad de código generado que era complicado de entender, revisar y validar y que no siempre cumplia con los requisitos minimos de calidad lo cual hacia que los PRs tengan muchas más idas y vueltas llegando a ser un proceso tedioso y frustrante
    - Hubo un momento de cambio a finales de octubre en el que el código de los PRs empezó a ser sospechosamente bueno y parecia que todo iba a ir funcionando de manera más coherente.

- El 21 de Octubre fue el release del libro de Vibe Coding que aproveche para leerlo en un par de días y sacar una cantidad de ideas y metodologías nuevas para aplicar.

- Soy  un very early adopter del uso intensivo de IA en muchas cosas, mayormente en el desarrollo de software pero tambien par otras cosas de las que quiero hablar en otros artículos. 


# intro al workflow

La idea principal de la metodologia es tener un proceso mucho más estructurado para aprovechar al máximo la IA, pero que a la vez sea flexible, adaptable a distintos tipos de problemas y sea extremadamente sencillo de aplicar.

Un par de suposiciones que tenemos que tener en cuenta y como yo interpreto a los modelos de lenguaje:

- Los modelos de lenguaje son Predictores de texto probabilísticos, exactamente como el completado automático del celular pero mucho más avanzado.
- No tienen memoria, no recuerdan nada de lo que pasó antes, solo lo que está en el contexto actual.
- El contexto es limitado, y cuanto más largo es el contexto, menos eficiente es el modelo para predecir la siguiente palabra.
- No son determinísticos, cada vez que les pedimos algo, pueden devolver resultados distintos.
- Los proveedores de modelos de lenguaje (anthropic, openai, google...) cobran por cantidad de tokens procesados, tanto de entrada como de salida. Y tenemos un presupuesto y uso limitado[^consumo-de-tokens].  
- cuanto mas lineal la cosa más sencilla. 

## Como estamos trabajando ahora

Está muy bueno pensar en como las herramientas que tenemos nos definen la forma que tenemos que trabajar. Hay veces
que tenemos que adaptarnos a las herramientas que tenemos y otras veces que abusamos de ellas de manera que hagan lo que queremos.

La vision de Emilio, tiro un insight muy importante ya hace 2 años, para entender hacia donde van a ir las cosas, la manera en la que vamos a terminar interactuando es a travez de un chat para todo. Lo cual de alguna manera tiene mucho sentido porque es la manera más sencilla de interactuar con un modelo de lenguaje que saber cuales son los 50 clicks y opciones, menues que hay que apretar para hacer algo especifico. Emilio contó que allá en los 90s (o antes) cuando empezaron a aparecer las primeras interfaces gráficas de usuario, había un debate muy grande sobre si las interfaces gráficas iban a reemplazar a las interfaces de línea de comando. Y al final lo que pasó es que las interfaces gráficas se impusieron porque eran mucho más sencillas de usar para la mayoría de la gente. Algo similar está pasando ahora con los modelos de lenguaje y las interfaces de chat.

Y eso se nota muchisimo en las herramientas que están apareciendo para el desarrollo de código con IA, y como los IDEs [^ide] donde uno desarrolla código están cada vez más orientados a tener un chat integrado para interactuar con un MdL/LLM[^mdl]. Bueno, a que va todo esto, es que la metodología actual que presentan estas herramientas como Cursor es de dos pasos uno de Planificación y otro de Implementación y esto queda un poco corto en algunos casos.

La propuesta de HumanLayer pueden verlo en la charla de Dex Horthly sobre Context Engineering[^context-engineering], es agregar un paso inicial de Investigación (Research) para poder tener un contexto mucho más claro y definido de lo que queremos hacer. Y esta separación es algo muy importante porque nos permite reducir el contexto sobre el cual queremos que el MdL nos devuelva una respuesta mucho más precisa, concreta y efectiva.

Para entender por que esto es así y para aprovechar al máximo el contexto tenemos que hacer un desvio y tratar de entender como funciona el contexto de los MdL.

NOTA: describir una analogia de una funcion sin estado y que tenga contexto limitado. Vamos a llamar contexto al texto que le pasamos como input para que el MdL genere una respuesta.

Algo que tenemos que tener en cuenta es:
- los MdL funcionan como una operación sin estado, esto quiere decir que cada vez que le pedimos algo no recuerdan nada de lo que pasó antes, solo lo que está en el contexto actual. Para simular la memoria tenemos que pasarle en el contexto toda la información que queremos que tenga en cuenta. [^memoria]
- los MdL son probabilísticos, esto quiere decir que no siempre nos van a devolver la misma respuesta dado un mismo contexto. 
- Los MdL estan entrenados con mucha informacion variada de todos lo que se les occurra y la manera en la que le proveemos el contexto delimita sobre que nos va a dar una respuesta, esto es algo que mejoró de manera impresionante en estos ultimos meses. 

Hagan el siguiente ejercicio para tratar de entender mejor estos conceptos:
Estamos en un almuerzo y hacemos una pregunta especifica sobre un tema muy puntual, por ejemplo: "Cuál es una buena comida para preparar?" 

La posibilidades de la respuesta son muchisimas, y van a depender de muchos factores, como por ejemplo:

- Quienes son nuestros amigos, cual es su cultura, no es lo mismo alguien del interior de Catamarca que alguien de Boston.


Pero podríamos mejorar un poco nuestra pregunta y eso va a hacer que la respuestas que nos den sean mucho más precisas y concretas. Por ejemplo, si le agregamos un poco más de contexto a nuestra pregunta, como por ejemplo: "Cuál es una buena comida para preparar en un almuerzo de domingo con amigos, que sea fácil de hacer y que guste a todos?"

Entonces restringimos un poco la respuesta, va a ser un almuerzo el domingo y con amigos, que no es lo mismo que algo para llevar un jueves a la oficina o una cena con alguien que querés impresionar. Podemos tambien hacer más explicito el tipo de comida, si es algo rápido, algo elaborado, si es comida vegetariana o no, etc, podemos decir los ingredientes que tenemos disponibles, el tiempo que tenemos para cocinar, etc. Cada dato adicional que agreguemos va a hacer la respuesta mucho más precisa y concreta.

Por ejemplo podríamos decir:
 "Cuál es una buena comida para preparar en un almuerzo de domingo con amigos, que sea fácil de hacer y que guste a todos? Tengo pollo, papas, ensalada y helado de postre."
 o incluso ser mucho más específicos: en los detalles de cantidades de cosas que tenemos, gustos ....

Tengo que preparar una comida para 6 amigos que vienen a almorzar el domingo a la tarde. Quiero que sea algo fácil de hacer, que no me lleve más de 1 hora de preparación y que guste a todos. Tengo  un pollo, 3kg papas, un par de tomates, un atado de rucula, creo que tengo zanahoria y unas manzanas. 

- el contexto es limitado, no le podemos pasar toda la información del universo de una sola sino que solo le podemos pasar una cantidad limitada de texto.
- la eficiencia de las respuestas decae a medida que el contexto se hace más largo

Para entender estos dos ultimos puntos pensemos en la siguiente analogía: 
Nos fuimos de camping y para lavar los platos tenemos que ir hasta el río con baldes a buscar agua. Entonces vamos a tener varias situaciones:
- Si tenemos que lavar un plato, con un balde de agua alcanza y sobra.
- Si tenemos que lavar 10 platos, con un balde de agua alcanza pero tenemos que ser cuidadosos de no desperdiciar agua. Y ser cuidadosos de no ensuciar el agua de manera innecesaria, porque a medida que vamos lavando más platos, el agua se va ensuciando y los platos quedan cada vez más sucios.
- Si tenemos que lavar 100 platos, con un balde de agua no alcanza, y vamos a tener que ir varias veces al río a buscar más agua. Y a medida que vamos lavando más platos, el agua se va ensuciando y los platos quedan cada vez más sucios.
- Y un punto  importante es que hay cosas que pueden contaminar completamente el contexto y derivarlo a algo inútil, por ejemplo si en el balde de agua lavamos un trapo con grasa, el agua va a quedar completamente inutilizable para lavar los platos.

Entonces, para poder aprovechar al máximo el contexto limitado que tenemos, tenemos que ser muy cuidadosos con lo que le pasamos al MdL, y tratar de ser lo más específicos y concretos posible. Y cuando el problema es muy grande,
 tenemos que dividir nuestro problema en partes más pequeñas y manejables. 

[^memoria]: algunas herramientas nos hacen creer que tienen memoria pero lo que están haciendo es agregar tras bambalinas informacion en el contexto.

[^mdl]: LLM es un Large Language Model. Es un tipo de programa basado en Inteligencia Artifical que está entrenado para entender y generar texto de manera similar a como lo haría un humano. 

[^ide]: Integrated Development Environment: Una especie de Photoshop pero en vez de para diseñar imágenes es para desarrollar código, suelen ser editores de texto que entienden la estrucura del código y proveen muchas herramientas para modificar, probar, investigar.

Como ultimo punto importate a notar es que existen distintas clases de MdL, algunos están optimizados para generar respuestas y algunos estan entrenados para utilizar herramientas, como por ejemplo, buscar en internet, buscar el los archivos de una computadora, ejecutar codigo, etc.


Ahora si entendiendo un poco más como funciona el contexto de los MdL podemos seguir:

Entonces el primer trabajo que tenemos que hacer es reducir generar el contexto necesario para que el MdL se enfoque lo más posible en la tarea que queremos hacer. Lo bueno es que no tenemos que hacer todo esto a mano, podemos pedirle al MdL que nos ayude a hacer este trabajo. Entonces la metodología que propongo es la siguiente:

# Empezar con la Investigación (Research)

- Dada una pregunta tratar de obtener toda la información relevante sobre el tema, por ejemplo cuando estamos trabajando con el codigo podemos pedirle  que investigue cuales son los archivos que son relevantes, cuales son las dependencias, que revise como interactuan los distintos componentes, si hay documentacion relevante, etc... 
Una vez que tiene toda esa informacion, le pedimos que cree un documento estructurado para poder pasarle en una nueva conversacion (lo que seria un nuevo balde) ese contexto reducido y relevante. 

Una vez que tenemos ese contexto reducido y relevante, lo que le pedimos es que realice una revisión crítica de la información que nos dió, para asegurarnos que no haya nada raro, nada que no tenga sentido, nada que esté mal. Esto es el segundo ingrediente de la metodología que Steve Yegge lo llama "La regla de los 5" (The Rule of 5) que una vez que uno tiene algo consiste en revisar varias veces la información bajo ciertos criterios.

Los pasos del Ro5 son:

1. Borrador (Draft): Crear el contenido inicial, no importa que sea perfecto, hay que asegurarse de que tenga lo necesario, preferir amplitud a profundidad.
2. Correctitud (Exactitud): Lo que contiene el documento es correcto?, arregla errores, problemas, inconsistencias.
Suele pasar que la documentacion que se leyo está desactualizada o es incorrecta, o que el MdL cometió errores en la interpretación de la información.
3. Claridad (Clarity): Alguien más puede entender esto?  Simplificalo, elimina todo lo innecesario, elimina la jerga, explica todo claramente. Suelen haber terminos especificos del proyecto, o el tema que estamos hablando que generan ambiguedad, o no estan del todo bien definidos, hay que asegurarse que todo esté bien explicado.
4. Casos límite (Edge Cases): Que podría salir mal? No estamos olvidando nada? Hay algo inusual que no estemos considerando? Hay alguna excepción? Asegurarse de que todo esté cubierto.
5. Excelencia (Excellence): Esto es lo mejor que podemos hacer? Hay alguna manera de mejorar esto? Alguna optimización, alguna mejora? Una vez que ya tenemos todo lo anterior, tratar de llevarlo a que sea lo mejor posiblo, se puede simplificar, hacer más eficiente, etc.

Entonces lo que tenemos que hacer es pedirle al MdL en una nueva conversación (un nuevo balde) que realice estos 5 pasos sobre la información que nos dió en el paso de investigación. Y es muy probable que aparezcan cosas nuevas que no habíamos considerado, errores, inconsistencias, etc. Esto lo podemos iterar tantas veces como haga falta hasta que estemos conformes con la calidad de la información.

Una vez que tenemos ya la investigación completa y revisada, lo que hacemos es pasarle ese contexto reducido y relevante a una nueva conversación (otro nuevo balde) y le pedimos que realice la planificación (Plan) y como es esperado despues aplicamos la Ro5 sobre el plan generado.

Algo importante del plan es que tiene que ser un plan de ejecución, no solo una lista de cosas a hacer, sino que tiene que tener un orden lógico, dependencias, tiempos estimados, etc. Y cada tarea tiene que ser lo suficientemente pequeña como para que pueda ser implementada en un solo paso sin excederce en el contexto, lo suficientemente delimitada para que podamos usar un único balde por cada tarea. Una forma bastante estrategica de hacegurarnos eso es dividir el plan en muchas subtareas y describir cada subtarea con el contexto necesario en una seccion distinta y con toda la información relevante para esa subtarea, nombres de archivos, topicos, dependencias, etc. En mi caso particular, luego de revisar el plan y que genera todas las tareas, nuevamente aplico la Ro5 sobre cada subtarea para asegurarme que cada una esté bien definida y sea lo suficientemente pequeña como para que pueda ser implementada en un solo paso.

Y como ultimo paso, ya con todas las tareas bien definidas y revisadas, pasamos a la implementación (Implement) donde cada tarea es implementada de manera independiente (un balde por tarea) validando que el comportamiento sea el esperado. Acá lo importante a notar es que ya tenemos casi totalmente definido que es lo que que se va a hacer. De manera que es algo casi deterministico y no hay mucho lugar para que el MdL se desvíe o invente cosas nuevas. Y la ventaja de esto es aprovechar la facilidad que tiene los MdL para ejecutar estas tareas pequeñas de manera rápida y eficiente, no les cuesta nada editar decenas de archivos, crear pruebas unitarias, etc, lo que como personas nos puede llevar mucho horas o más, pero para un MdL es cuestión de segundos.

Y una vez que tenemos toda la implementación lista, volvemos a aplicar la Ro5 sobre el conjunto completo para asegurarnos que todo esté bien integrado, que no haya errores, que todo funcione como se espera.

Esto es algo que normalmente se describe como "shift-left" que es llevar un proceso el cual nos permita detectar desvios o errores lo más temprano posible en el proceso, para evitar tener que volver atrás y rehacer cosas. Y esto es algo que los MdL pueden hacer muy bien, porque pueden revisar y validar cosas de manera rápida y eficiente. 

Un punto importante que menciona la gente de HumanLayer es que un prompt incorrecto puede generar una centena de lineas de código incorrecto, que un plan mal definido puede generar decenas de miles de lineas de código incorrecto. Y que una investigación incompleta puede llevarnos a desperdiciar mucho tiempo y recursos en cosas que no son relevantes o no tienen sentido. Por eso es tan importante tener un proceso estructurado y riguroso para aprovechar al máximo el potencial de los MdL y lo más importante es que tenemos que revisar todos los artefactos que generamos en cada paso. El documento de Research tiene que ser revisado de manera exhaustiva por una o varias personas para validar que lo que se va a hacer está bien, lo mismo con el plan, los modelos son muy buenos, pero siempre hay cosas que se les escapan porque no existen de manera concreta en los materiales del proyecto, son ideas o conocimiento que está implicito en la cabeza de las personas y esto es una gran oportunidad de hacerlas explicitas.

En el caso del desarrollo de código yo puedo decir que en el día de hoy, puedo utilizar modelos de lenguague para generar código que es muchisimo mejor de lo que podría hacer por mi cuenta y en tiempos muy cortos. Y esto tiene consecuencias muy claras que voy a discutir más abajo.


Resumiendo el proceso tenemos 

Investigación -> Plan -> Implementación, con un ciclo interno del Regla de los 5 en cada paso.

Lo importante de tenerlo separado, es que los artefactos que se producen están disponibles para revisar y corregir.
Si lo que hacemos es mandarlo todo de una vamos a seguir quemando arboles por el gusto de simplemente ver como se quema un arbol.


# Reutilizando la metodología

Lo bueno de este proceso es que es reutilizable para generar artefactos que nos permitar contextualizar nuestras
revisiones o los pasos de manera más explicita. Por ejemplo, podemos tener "prompts" específicos para realizar los pasos de investigación para el tipo de problema o proceso que queremos resolver. 

Por ejemplo, las cosas que tiene Charly respecto de tener distintas visiones de como realizar la implementación de un código, cuales son las preferencias y todo eso. En las que aprobechó Gemini Deep Research para armar investigar metodologías y protocolos existentes en distintas profesiones para asegurarse de que lo que se realiza va a salir bien, imaginensé el lanzar un cohete al espacio, hacer una cirugía a corazón abierto, organizar un mundial de fútbol, invadir un país. Todo eso requiere procedimientos y metodologías que ya están recontra mega archi estudiadas y ahora las podemos aprobechar para que un MdL nos ayude a implementarlas en nuestros procesos.





