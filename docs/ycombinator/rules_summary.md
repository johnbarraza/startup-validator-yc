# 📋 Reglas YC Completas + Preguntas de Validación
> Extraídas de los videos de Y Combinator y documentos de referencia

---

## 🎬 VIDEO 1: "Pick One Idea and Go Deep"

### Reglas derivadas
| # | Regla | Aplicación a MineAssist-PdM |
|---|-------|-----------------------------|
| R1 | **No busques la idea perfecta.** Sal a la realidad. La idea se descubre con feedback real de clientes, no en abstracto. | No esperar tener acceso a una mina real. Validar con CWRU + entrevistas a técnicos de mantenimiento. |
| R2 | **Quema los barcos.** Trabaja en una sola idea a la vez. Múltiples ideas simultáneas generan señales de mala calidad. | No mezclar el trabajo de MineAssist con las ideas de app de estudio o fitness. Una a la vez. |
| R3 | **Estándar de Oro:** ¿Podrías dirigir el negocio de tu cliente? Si no sabes cuáles son sus crisis diarias, no estás lo suficientemente adentro. | Pregunta de auditoría: ¿Puedes describir el día a día de un jefe de mantenimiento de Las Bambas? ¿Sabes qué le quita el sueño? |
| R4 | **Construye en el filo de la IA.** El producto debe mejorar automáticamente conforme mejoren los modelos subyacentes. | La capa de explicabilidad con LLM mejorará sola. Pero el moat (datos de vibración + lógica de dominio minero) debe ser propio. |
| R5 | **Verticaliza: vende el resultado, no la herramienta.** No "software de monitoreo", sino "cero paradas no programadas". | Pricing por outcome (por activo protegido, por parada evitada) en lugar de por "asientos" o "usuarios". |
| R6 | **Ambición extrema.** El costo de esfuerzo de una idea ambiciosa es similar al de una modesta. | No detenerse en "dashboard de vibraciones". La versión ambiciosa: ser el "sistema nervioso digital" de la planta minera. |
| R7 | **El fracaso te da datos estructurales.** Si la idea no funciona, aprendiste dónde está el problema real que sí vale la pena resolver. | Documentar cada pivote con evidencia. No tirar el trabajo; guardarlo como Phase 0 Data. |

### ❓ Preguntas para hacerse en cada sesión (Checklist del video 1)
- [ ] ¿Estoy trabajando en una sola idea hoy?
- [ ] ¿Podría describir el flujo de trabajo diario de mi cliente objetivo sin dudarlo?
- [ ] ¿Mis decisiones de hoy me acercan a un cliente real o solo a más código?
- [ ] ¿La versión actual del producto vende un resultado o una funcionalidad?

---

## 🎬 VIDEO 2: "How to Build an AI-Native Services Company"

### Reglas derivadas
| # | Regla | Aplicación a MineAssist-PdM |
|---|-------|-----------------------------|
| R8 | **Elige mercados con baja confianza y alta inteligencia requerida.** Trabajo tercerizado + alto umbral de expertise + entorno regulado = moat natural. | La minería cumple los tres: tercerizada (contratas mecánicas), requiere ingenieros especializados (escasos) y es regulada (OSINERGMIN). |
| R9 | **El proceso ES el producto.** Enfócate en reducir la varianza de los outputs, no solo en mejorar el promedio. La inconsistencia destruye la confianza. | Cada explicación de IA debe tener el mismo nivel de calidad. Implementar fallback determinista + logging de outputs. |
| R10 | **Evita la "trampa de la demanda temprana".** Demasiados pilotos simultáneos destruyen tu capacidad de construir. Calidad antes que cantidad. | No aceptar más de 2 clientes piloto al mismo tiempo en la fase inicial. |
| R11 | **Vende outcomes con pricing por unidad o resultado.** No por asientos, no por tokens. | Pricing: por activo monitorizado / mes. No por "usuario" ni por "llamadas a la API". |
| R12 | **Obsesiónate con el COGS (Costo de bienes vendidos).** Apunta a márgenes de software (50%+), no de firma de servicios (30%). | Calcular: costo de inferencia LLM por reporte generado + costo de hosting. El objetivo es <$0.05 USD por predicción+explicación. |
| R13 | **No "añadas IA" a un negocio legacy.** Empieza desde cero con mentalidad AI-native. | No intentar integrarse a SAP PM. Ser el reemplazo simple y barato desde el día 1. |
| R14 | **El equipo fundador necesita 3 fluencias:** dominio (minería), modelo (IA) y rigor operacional (gestionar throughput). | En el contexto de solo founder: el agente IA cubre la fluencia de modelo, el founder cubre dominio y operación. |

### ❓ Preguntas para hacerse en cada sesión (Checklist del video 2)
- [ ] ¿El mercado que estoy atacando tiene trabajo tercerizado con alta fricción de conocimiento?
- [ ] ¿El output de la IA tiene varianza controlada? ¿Tengo logging de cada resultado?
- [ ] ¿Sé exactamente cuánto me cuesta generar un reporte de predicción + explicación?
- [ ] ¿El modelo de precios es por resultado/unidad, no por usuario?

---

## 🎬 VIDEO 3: "How to Get and Evaluate Startup Ideas" (Jared Friedman - YC)

### Las 10 preguntas de evaluación de Friedman
Aplicadas directamente a MineAssist-PdM:

| # | Pregunta | Respuesta Honesta para MineAssist-PdM |
|---|----------|---------------------------------------|
| Q1 | **¿Tienes founder-market fit?** | Moderado. Formación en Data Science + economía. Falta: experiencia directa en campo minero. Mitigar: entrevistas intensivas a técnicos. |
| Q2 | **¿Qué tan grande es el mercado?** | Enorme. TAM $4.2B global, SAM $350M Latinoamérica. Minería es el sector #1 exportador del Perú. |
| Q3 | **¿Qué tan agudo es el problema?** | Muy agudo. Sin solución = $50K-$150K/hora de pérdida. Las alternativas actuales son Excel y visitas mensuales de técnicos. |
| Q4 | **¿Hay competencia?** | Sí (SAP PM, OSIsoft, Aspentech). Eso valida el mercado. Nuestro diferencial: precio 10x menor + explicabilidad en español + sin integración ERP compleja. |
| Q5 | **¿Lo quieres tú personalmente?** | Sí, como proyecto de DS + impacto en la industria más importante del Perú. |
| Q6 | **¿Recientemente posible/necesario?** | Sí. LLMs baratos (2023+), sensores IoT económicos, dataset CWRU público, regulación de SSO minera más estricta. |
| Q7 | **¿Existen proxies?** | Sí. Uptake (USA, minería), SparkCognition (industria pesada), Augury (manufacturing). Todos con valuaciones >$500M. |
| Q8 | **¿Trabajarías en esto años?** | Sí. La industria minera peruana es lo suficientemente profunda para años de trabajo. |
| Q9 | **¿Es escalable?** | Sí. Modelo de ML entrena una vez. El LLM escala con tokens. No requiere más ingenieros por cada cliente adicional. |
| Q10 | **¿Es un buen espacio de idea?** | Sí. Industrial AI / Predictive Maintenance tiene track record de salidas exitosas (Rockwell, GE, ABB adquiriendo startups). |
| Q11 | **¿Lo googleaste? ¿Revisaste Play Store y Reddit?** | Pendiente. Buscar en r/mining, r/CMMS, r/industrialautomation. |

### Errores a evitar (del video 3)
- ❌ **"Solución en busca de problema":** No construir features de IA que nadie pidió. Cada feature debe nacer de una queja real de un técnico.
- ❌ **"Tar Pit Ideas":** Evitar ideas que parecen fáciles pero tienen barreras estructurales ocultas (ej. "dashboards genéricos" sin integración real).
- ❌ **Esperar la idea perfecta:** Lanzar un MVP funcional (aunque sea con datos sintéticos) es mejor que planificar sin ejecutar.

### ❓ Preguntas para hacerse antes de cada sprint de desarrollo
- [ ] ¿Este feature nació de una queja real de un cliente/usuario?
- [ ] ¿Ya busqué si existe algo así en Reddit, Play Store, Product Hunt?
- [ ] ¿Cuál es el proxy de éxito que valida que este mercado funciona?
- [ ] ¿Estoy construyendo para el mercado más grande posible dentro de mi nicho?

---

## 🔥 Checklist Maestro: Antes de Arrancar Cada Sesión
> Responder estas preguntas toma 5 minutos y evita días de trabajo en la dirección equivocada.

**Foco:**
- [ ] ¿En qué única idea estoy trabajando hoy?
- [ ] ¿Qué aprendí del mercado/cliente desde la última sesión?

**Profundidad:**
- [ ] ¿Podría describir el día de trabajo de mi cliente objetivo sin dudarlo?
- [ ] ¿Tengo al menos 1 entrevista de cliente pendiente de agendar?

**Producto:**
- [ ] ¿El output de IA de hoy tiene varianza controlada?
- [ ] ¿Sé cuánto cuesta generar 1 predicción + explicación?

**Validación:**
- [ ] ¿El feature que voy a construir resuelve un dolor específico documentado?
- [ ] ¿Hay evidencia de que alguien pagaría por esto?
