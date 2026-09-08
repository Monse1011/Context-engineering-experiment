# Context-engineering-experiment



<table>
  <thead>
    <tr>
      <th>Métricas</th>
      <th>A</th>
      <th>B</th>
      <th>C</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Test passing</td>
      <td>4/4</td>
      <td>4/4</td>
      <td>4/4</td>
    </tr>
    <tr>
      <td>Test falling</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
    </tr>
       <tr>
      <td>Requisitos cumplidos</td>
      <td>Todos los solicitados</td>
      <td>Todos los solicitados</td>
      <td>Todos los solicitados</td>
    </tr>
    <tr>
      <td>Archivos modificados</td>
      <td>2</td>
      <td>2</td>
      <td>2</td>
    </tr>
    <tr>
      <td>Cambios innecesarios</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <td>Intervensiones humana</td>
      <td>10</td>
      <td>16</td>
      <td>9</td>
    </tr>
    <tr>
      <td>Problemas introducidos</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <td>Tiempo</td>
      <td>5 min</td>
      <td>3 min</td>
      <td>3 min</td>
    </tr>
    <tr>
      <td>Score</td>
      <td>9</td>
      <td>9.5</td>
      <td>110</td>
    </tr>
  </tbody>
</table>


<h3>¿Cuál fue tu hipótesis?</h3>
La hipotesis fue que entre más contexto le demos al agente mejor va a realizar la tarea solicitada y requieriendo menos ayuda humana.
<h3>¿Cuál experimento produjo el menor resultado y porque? </h3>
Todos produjeron el mismo resultado, pero el experimento c donde le damos el SPEC y el agente fue mucho más rápido y requirió menos intervensión humana.
<h3> ¿Qué errores aparecieron en A y no en C?</h3>
Considero que al ser un proyecto tan pequeño no habia margen para ingresar errores. Al final todos los experimentos llegaron a lo mismo.
<h3>¿Qué información del repositorio fue más útil?</h3>
La del experimento C
<h3>¿Qué aportó SPEC.md?</h3>
Aportó lo que el modelo debía de hacer, los requerimientos, los criterios de aceptación para que no haya margen de fallar.
<h3>¿Qué función tuvo AGENTS.md?</h3>
Le dijó al modelo lo que tenía que realizar, los pasos para que no se perdiera y fuera mas conciso en su proceso. 
<h3>¿Más contexto significa necesariamente mejor contexto?</h3>
No necesariamente si no es contexto de calidad, si bien darle mucha información puede ser útil también puede ser contraproducente ya que la información del contexto puede que sea irrelevante.
<h3>¿Qué intervención humana fue necesaria?</h3>
Solo aceptar cambios y comandos que se necesitaban realizar para poder ver el repositoria, ejecutar los tests, etc.
<h3>¿Qué cambiarías en SPEC.md y AGENTS.md?</h3>
Creo que fueron muy utiles asi como se encuentran. 
<h3> ¿Qué aprendiste sobre la responsabilidad del desarrollador al usar agentes?</h3>
Aprendí que debemos de ser concretos y concisos a la hora de definir los contextos y son de gran ayuda para obtener un mejor resultado.


<h3>¿Por qué un desarrollador que utiliza agentes de código necesita aprender Context Engineering y no solamente mejores prompts?</h3>

Porque los prompts solo dice lo que se debe hacer, si bien es util un mejor prompt para evitar desperdiciar tokens, el contexto hace que sea mas concreto la tarea, dando info extra sobre lo que se debe realizaar, sobre los criterios de aceptación etc.



