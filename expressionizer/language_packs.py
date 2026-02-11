from __future__ import annotations

import re
from typing import Literal


StyleType = Literal["default", "compact", "plain", "xml"]


_EN_MESSAGES: dict[str, str] = {
    "step.heading": "## {number}",
    "calculator.fallback": "$$ {expression} = {result} $$",
    "substitution.separator_pair": " and ",
    "substitution.separator_many": ", ",
    "manual_review.title": "# Manual Verification Cases",
    "manual_review.subtitle": "Use this file to manually review generated problems, answers, and step-by-step explanations.",
    "manual_review.case": "Case",
    "manual_review.problem": "Problem",
    "manual_review.answer": "Answer",
    "manual_review.status": "Solve status",
    "manual_review.reason_code": "reason_code",
    "manual_review.approximate": "approximate",
    "equation_manual_review.title": "# Equation Manual Verification Cases",
    "equation_manual_review.subtitle": "Generated equation/system problems with native step-by-step solutions.",
    "equation_manual_review.case": "Case",
    "equation_manual_review.problem": "Problem",
    "equation_manual_review.solution": "Solution",
    "equation_manual_review.status": "Solve status",
    "equation_manual_review.reason_code": "reason_code",
    "equation.unsupported_equation_arity": "Only two-sided equations are supported in this solver.",
    "equation.linear.multiple_variables": "Multiple variables remain. Pass `variable=` to solve for a specific one.",
    "equation.linear.identity": "The equation simplifies to $0 = 0$, so infinitely many solutions exist.",
    "equation.linear.contradiction": "The equation simplifies to a contradiction, so there is no solution.",
    "equation.nonlinear.target_variable_required": "Nonlinear native solving requires a single target variable. Pass `variable=` explicitly.",
    "equation.nonlinear.unsupported_pattern": "This nonlinear equation is outside native-supported patterns, so it is left unsolved.",
    "system.empty": "No equations were provided.",
    "system.unsupported_equation_arity": "Each equation must have exactly two sides.",
    "system.nonlinear_or_unsupported": "At least one equation is nonlinear or unsupported.",
    "system.no_variables": "The system has no variables after simplification.",
    "system.inconsistent": "A row reduced to $0 = c$ with $c \\neq 0$, so the system is inconsistent.",
    "system.infinite_solutions": "Not every variable has a pivot; the system has infinitely many solutions.",
    "substitution_intro": "Substitute values: {substitutions}.",
    "derivative_result": "Applied differentiation rules.",
    "minus_one_power_parity": "$-1^{{{exponent}}}$ depends on parity; result is ${result}$.",
    "render.step.joiner": "\n\n",
    "render.substep.joiner": "\n",
}


_ES_MESSAGES = {
    "step.heading": "## Paso {number}",
    "calculator.fallback": "$$ {expression} = {result} $$",
    "substitution.separator_pair": " y ",
    "substitution.separator_many": ", ",
    "manual_review.title": "# Casos de Verificacion Manual",
    "manual_review.subtitle": "Usa este archivo para revisar manualmente problemas generados, respuestas y explicaciones paso a paso.",
    "manual_review.case": "Caso",
    "manual_review.problem": "Problema",
    "manual_review.answer": "Respuesta",
    "manual_review.status": "Estado",
    "manual_review.reason_code": "codigo_razon",
    "manual_review.approximate": "aproximado",
    "equation_manual_review.title": "# Casos de Verificacion Manual de Ecuaciones",
    "equation_manual_review.subtitle": "Problemas de ecuaciones/sistemas generados con soluciones nativas paso a paso.",
    "equation_manual_review.case": "Caso",
    "equation_manual_review.problem": "Problema",
    "equation_manual_review.solution": "Solucion",
    "equation_manual_review.status": "Estado",
    "equation_manual_review.reason_code": "codigo_razon",
    "equation.unsupported_equation_arity": "Este solucionador solo admite ecuaciones con dos lados.",
    "equation.linear.identity": "La ecuacion se simplifica a $0 = 0$, por lo que hay infinitas soluciones.",
    "equation.linear.contradiction": "La ecuacion se simplifica a una contradiccion, por lo que no hay solucion.",
    "equation.linear.multiple_variables": "Quedan varias variables. Usa `variable=` para resolver una variable especifica.",
    "equation.nonlinear.target_variable_required": "La resolucion nativa no lineal requiere una sola variable objetivo. Pasa `variable=`.",
    "equation.nonlinear.unsupported_pattern": "Esta ecuacion no lineal esta fuera de los patrones nativos compatibles y queda sin resolver.",
    "system.unsupported_equation_arity": "Cada ecuacion debe tener exactamente dos lados.",
    "system.nonlinear_or_unsupported": "Al menos una ecuacion es no lineal o no compatible.",
    "system.no_variables": "El sistema no tiene variables tras simplificar.",
    "system.inconsistent": "Una fila se redujo a $0 = c$ con $c \\neq 0$, por lo que el sistema es inconsistente.",
    "system.infinite_solutions": "No toda variable tiene pivote; el sistema tiene infinitas soluciones.",
    "system.empty": "No se proporcionaron ecuaciones.",
    "substitution_intro": "Sustituye los valores: {substitutions}.",
    "derivative_result": "Se aplicaron reglas de derivacion.",
    "minus_one_power_parity": "$-1^{{{exponent}}}$ depende de la paridad; el resultado es ${result}$.",
}

_FR_MESSAGES = {
    "step.heading": "## Etape {number}",
    "calculator.fallback": "$$ {expression} = {result} $$",
    "substitution.separator_pair": " et ",
    "substitution.separator_many": ", ",
    "manual_review.title": "# Cas de Verification Manuelle",
    "manual_review.subtitle": "Utilisez ce fichier pour verifier manuellement les problemes generes, les reponses et les explications etape par etape.",
    "manual_review.case": "Cas",
    "manual_review.problem": "Probleme",
    "manual_review.answer": "Reponse",
    "manual_review.status": "Statut",
    "manual_review.reason_code": "code_raison",
    "manual_review.approximate": "approxime",
    "equation_manual_review.title": "# Cas de Verification Manuelle des Equations",
    "equation_manual_review.subtitle": "Problemes d'equations/systemes generes avec des solutions natives etape par etape.",
    "equation_manual_review.case": "Cas",
    "equation_manual_review.problem": "Probleme",
    "equation_manual_review.solution": "Solution",
    "equation_manual_review.status": "Statut",
    "equation_manual_review.reason_code": "code_raison",
    "equation.unsupported_equation_arity": "Ce solveur prend uniquement en charge les equations a deux membres.",
    "equation.linear.identity": "L'equation se simplifie en $0 = 0$, donc il existe une infinite de solutions.",
    "equation.linear.contradiction": "L'equation se simplifie en contradiction, donc il n'y a pas de solution.",
    "equation.linear.multiple_variables": "Plusieurs variables restent. Passez `variable=` pour en isoler une.",
    "equation.nonlinear.target_variable_required": "La resolution native non lineaire necessite une variable cible unique. Passez `variable=`.",
    "equation.nonlinear.unsupported_pattern": "Cette equation non lineaire est hors des motifs natifs pris en charge et reste non resolue.",
    "system.unsupported_equation_arity": "Chaque equation doit avoir exactement deux membres.",
    "system.nonlinear_or_unsupported": "Au moins une equation est non lineaire ou non prise en charge.",
    "system.no_variables": "Le systeme ne contient plus de variables apres simplification.",
    "system.inconsistent": "Une ligne reduite a $0 = c$ avec $c \\neq 0$ rend le systeme incoherent.",
    "system.infinite_solutions": "Toutes les variables n'ont pas de pivot; le systeme admet une infinite de solutions.",
    "system.empty": "Aucune equation fournie.",
    "substitution_intro": "Substituez les valeurs : {substitutions}.",
    "derivative_result": "Regles de derivation appliquees.",
    "minus_one_power_parity": "$-1^{{{exponent}}}$ depend de la parite; le resultat est ${result}$.",
}

_DE_MESSAGES = {
    "step.heading": "## Schritt {number}",
    "calculator.fallback": "$$ {expression} = {result} $$",
    "substitution.separator_pair": " und ",
    "substitution.separator_many": ", ",
    "manual_review.title": "# Manuelle Verifikationsfalle",
    "manual_review.subtitle": "Verwenden Sie diese Datei, um generierte Aufgaben, Antworten und Schritt-fur-Schritt-Erklarungen manuell zu prufen.",
    "manual_review.case": "Fall",
    "manual_review.problem": "Aufgabe",
    "manual_review.answer": "Antwort",
    "manual_review.status": "Status",
    "manual_review.reason_code": "grund_code",
    "manual_review.approximate": "approx",
    "equation_manual_review.title": "# Manuelle Verifikationsfalle fur Gleichungen",
    "equation_manual_review.subtitle": "Generierte Gleichungs-/Systemaufgaben mit nativen Schritt-fur-Schritt-Losungen.",
    "equation_manual_review.case": "Fall",
    "equation_manual_review.problem": "Aufgabe",
    "equation_manual_review.solution": "Losung",
    "equation_manual_review.status": "Status",
    "equation_manual_review.reason_code": "grund_code",
    "equation.unsupported_equation_arity": "Dieser Loser unterstutzt nur zweiseitige Gleichungen.",
    "equation.linear.identity": "Die Gleichung vereinfacht sich zu $0 = 0$, daher gibt es unendlich viele Losungen.",
    "equation.linear.contradiction": "Die Gleichung vereinfacht sich zu einem Widerspruch, daher gibt es keine Losung.",
    "equation.linear.multiple_variables": "Mehrere Variablen bleiben ubrig. Mit `variable=` eine Zielvariable angeben.",
    "equation.nonlinear.target_variable_required": "Nichtlineares natives Losen erfordert genau eine Zielvariable. `variable=` angeben.",
    "equation.nonlinear.unsupported_pattern": "Diese nichtlineare Gleichung liegt auerhalb der nativ unterstutzten Muster und bleibt ungelost.",
    "system.unsupported_equation_arity": "Jede Gleichung muss genau zwei Seiten haben.",
    "system.nonlinear_or_unsupported": "Mindestens eine Gleichung ist nichtlinear oder nicht unterstutzt.",
    "system.no_variables": "Das System hat nach der Vereinfachung keine Variablen.",
    "system.inconsistent": "Eine Zeile wurde zu $0 = c$ mit $c \\neq 0$ reduziert; das System ist inkonsistent.",
    "system.infinite_solutions": "Nicht jede Variable hat ein Pivot; das System hat unendlich viele Losungen.",
    "system.empty": "Keine Gleichungen wurden angegeben.",
    "substitution_intro": "Setze die Werte ein: {substitutions}.",
    "derivative_result": "Ableitungsregeln wurden angewendet.",
    "minus_one_power_parity": "$-1^{{{exponent}}}$ hangt von der Paritat ab; Ergebnis ist ${result}$.",
}

_KO_MESSAGES = {
    "step.heading": "## 단계 {number}",
    "calculator.fallback": "$$ {expression} = {result} $$",
    "substitution.separator_pair": " 및 ",
    "substitution.separator_many": ", ",
    "manual_review.title": "# 수동 검증 사례",
    "manual_review.subtitle": "이 파일을 사용해 생성된 문제, 정답, 단계별 설명을 수동으로 검토하세요.",
    "manual_review.case": "사례",
    "manual_review.problem": "문제",
    "manual_review.answer": "정답",
    "manual_review.status": "해결 상태",
    "manual_review.reason_code": "사유 코드",
    "manual_review.approximate": "근사 여부",
    "equation_manual_review.title": "# 방정식 수동 검증 사례",
    "equation_manual_review.subtitle": "네이티브 단계별 풀이가 포함된 방정식/연립방정식 생성 사례입니다.",
    "equation_manual_review.case": "사례",
    "equation_manual_review.problem": "문제",
    "equation_manual_review.solution": "해",
    "equation_manual_review.status": "해결 상태",
    "equation_manual_review.reason_code": "사유 코드",
    "equation.unsupported_equation_arity": "이 풀이기는 양변 형태의 방정식만 지원합니다.",
    "equation.linear.identity": "방정식이 $0 = 0$으로 단순화되어 해가 무한히 많습니다.",
    "equation.linear.contradiction": "방정식이 모순으로 단순화되어 해가 없습니다.",
    "equation.linear.multiple_variables": "여러 변수가 남아 있습니다. 특정 변수를 풀려면 `variable=`를 지정하세요.",
    "equation.nonlinear.target_variable_required": "비선형 네이티브 풀이에는 단일 대상 변수가 필요합니다. `variable=`를 지정하세요.",
    "equation.nonlinear.unsupported_pattern": "이 비선형 방정식은 네이티브 지원 패턴 범위를 벗어나 해결하지 않습니다.",
    "system.unsupported_equation_arity": "각 방정식은 정확히 두 변을 가져야 합니다.",
    "system.nonlinear_or_unsupported": "최소 한 개의 방정식이 비선형이거나 지원되지 않습니다.",
    "system.no_variables": "단순화 후 시스템에 변수가 없습니다.",
    "system.inconsistent": "한 행이 $0 = c$ (단, $c \\neq 0$)로 줄어들어 시스템이 모순입니다.",
    "system.infinite_solutions": "모든 변수에 피벗이 없어 해가 무한히 많습니다.",
    "system.empty": "제공된 방정식이 없습니다.",
    "substitution_intro": "값을 대입합니다: {substitutions}.",
    "derivative_result": "미분 규칙을 적용했습니다.",
    "minus_one_power_parity": "$-1^{{{exponent}}}$은(는) 짝홀성에 따라 값이 달라지며 결과는 ${result}$입니다.",
}

_HE_MESSAGES = {
    "step.heading": "## שלב {number}",
    "calculator.fallback": "$$ {expression} = {result} $$",
    "substitution.separator_pair": " ו-",
    "substitution.separator_many": ", ",
    "manual_review.title": "# מקרי אימות ידני",
    "manual_review.subtitle": "השתמשו בקובץ זה כדי לסקור ידנית בעיות שנוצרו, תשובות והסברים שלב-אחר-שלב.",
    "manual_review.case": "מקרה",
    "manual_review.problem": "שאלה",
    "manual_review.answer": "תשובה",
    "manual_review.status": "סטטוס פתרון",
    "manual_review.reason_code": "קוד סיבה",
    "manual_review.approximate": "בקירוב",
    "equation_manual_review.title": "# מקרי אימות ידני למשוואות",
    "equation_manual_review.subtitle": "בעיות משוואות/מערכות שנוצרו עם פתרונות מובנים שלב-אחר-שלב.",
    "equation_manual_review.case": "מקרה",
    "equation_manual_review.problem": "שאלה",
    "equation_manual_review.solution": "פתרון",
    "equation_manual_review.status": "סטטוס פתרון",
    "equation_manual_review.reason_code": "קוד סיבה",
    "equation.unsupported_equation_arity": "הפותר תומך רק במשוואות דו-אגפיות.",
    "equation.linear.identity": "המשוואה מצטמצמת ל-$0 = 0$, ולכן יש אינסוף פתרונות.",
    "equation.linear.contradiction": "המשוואה מצטמצמת לסתירה, ולכן אין פתרון.",
    "equation.linear.multiple_variables": "נותרו כמה משתנים. העבר/י `variable=` כדי לפתור עבור משתנה מסוים.",
    "equation.nonlinear.target_variable_required": "פתרון לא-לינארי מובנה דורש משתנה יעד יחיד. העבר/י `variable=`.",
    "equation.nonlinear.unsupported_pattern": "המשוואה הלא-לינארית הזו מחוץ לתבניות הנתמכות באופן מובנה ולכן לא נפתרת.",
    "system.unsupported_equation_arity": "לכל משוואה חייבים להיות בדיוק שני אגפים.",
    "system.nonlinear_or_unsupported": "לפחות אחת מהמשוואות אינה לינארית או אינה נתמכת.",
    "system.no_variables": "למערכת אין משתנים לאחר פישוט.",
    "system.inconsistent": "שורה הצטמצמה ל-$0 = c$ כאשר $c \\neq 0$, ולכן המערכת אינה עקבית.",
    "system.infinite_solutions": "לא לכל משתנה יש ציר; למערכת יש אינסוף פתרונות.",
    "system.empty": "לא סופקו משוואות.",
    "substitution_intro": "מציבים את הערכים: {substitutions}.",
    "derivative_result": "יושמו כללי הגזירה.",
    "minus_one_power_parity": "$-1^{{{exponent}}}$ תלוי בזוגיות; התוצאה היא ${result}$.",
}

_HE_NIQQUD_MESSAGES = {
    "step.heading": "## שָׁלָב {number}",
    "calculator.fallback": "$$ {expression} = {result} $$",
    "substitution.separator_pair": " וְ-",
    "substitution.separator_many": ", ",
    "manual_review.title": "# מִקְרֵי אִמּוּת יָדָנִי",
    "manual_review.subtitle": "הִשְׁתַּמְּשׁוּ בְּקוֹבֶץ זֶה כְּדֵי לִסְקוֹר יָדָנִית בְּעָיוֹת שֶׁנּוֹצְרוּ, תְּשׁוּבוֹת וְהַסְבָּרִים שָׁלָב־אַחַר־שָׁלָב.",
    "manual_review.case": "מִקְרֶה",
    "manual_review.problem": "שְׁאֵלָה",
    "manual_review.answer": "תְּשׁוּבָה",
    "manual_review.status": "סְטָטוּס פִּתְרוֹן",
    "manual_review.reason_code": "קוֹד סִבָּה",
    "manual_review.approximate": "בְּקֵירוּב",
    "manual_review.generator_meta": "- מִשְׁפַּחַת יְצִירָה: `{family}` | סִבַּת אִי־פְּתִירוּת מְכֻוֶּנֶת: `{reason}`",
    "equation_manual_review.title": "# מִקְרֵי אִמּוּת יָדָנִי לְמִשְׁוָאוֹת",
    "equation_manual_review.subtitle": "בְּעָיוֹת מִשְׁוָאוֹת/מַעֲרָכוֹת שֶׁנּוֹצְרוּ עִם פִּתְרוֹנוֹת מוּבְנִים שָׁלָב־אַחַר־שָׁלָב.",
    "equation_manual_review.case": "מִקְרֶה",
    "equation_manual_review.problem": "שְׁאֵלָה",
    "equation_manual_review.solution": "פִּתְרוֹן",
    "equation_manual_review.status": "סְטָטוּס פִּתְרוֹן",
    "equation_manual_review.reason_code": "קוֹד סִבָּה",
    "equation.unsupported_equation_arity": "הַפּוֹתֵר תּוֹמֵךְ רַק בְּמִשְׁוָאוֹת דּוּ־אַגַּפִּיּוֹת.",
    "equation.linear.identity": "הַמִּשְׁוָאָה מִצְטַמְצֶמֶת לְ-$0 = 0$, וְלָכֵן יֵשׁ אֵין־סוֹף פִּתְרוֹנוֹת.",
    "equation.linear.contradiction": "הַמִּשְׁוָאָה מִצְטַמְצֶמֶת לִסְתִירָה, וְלָכֵן אֵין פִּתְרוֹן.",
    "equation.linear.multiple_variables": "נוֹתְרוּ מִסְפָּר מִשְׁתַּנִּים. הַעֲבִירוּ `variable=` כְּדֵי לִפְתּוֹר עֲבוּר מִשְׁתַּנֶּה מְסֻיָּם.",
    "equation.nonlinear.target_variable_required": "פִּתְרוֹן לֹא־לִינֵאָרִי מוּבְנֶה דּוֹרֵשׁ מִשְׁתַּנֶּה יַעַד יָחִיד. הַעֲבִירוּ `variable=`.",
    "equation.nonlinear.unsupported_pattern": "הַמִּשְׁוָאָה הַלֹּא־לִינֵאָרִית הַזֹּאת מִחוּץ לַתַּבְנִיּוֹת הַנִּתְמָכוֹת בְּאֹפֶן מוּבְנֶה, וְלָכֵן אֵינָהּ נִפְתֶּרֶת.",
    "equation.rational.identity_domain": "$$ \\text{זֶהוּת בַּתְּחוּם} $$",
    "system.unsupported_equation_arity": "לְכָל מִשְׁוָאָה חַיָּבִים לִהְיוֹת בְּדִיּוּק שְׁנֵי אֲגַפִּים.",
    "system.nonlinear_or_unsupported": "לְפָחוֹת אַחַת מֵהַמִּשְׁוָאוֹת אֵינָהּ לִינֵאָרִית אוֹ אֵינָהּ נִתְמֶכֶת.",
    "system.no_variables": "לַמַּעֲרֶכֶת אֵין מִשְׁתַּנִּים לְאַחַר פִּשּׁוּט.",
    "system.inconsistent": "שׁוּרָה הִצְטַמְצְמָה לְ-$0 = c$ כַּאֲשֶׁר $c \\neq 0$, וְלָכֵן הַמַּעֲרֶכֶת אֵינָהּ עֲקִיבָה.",
    "system.infinite_solutions": "לֹא לְכָל מִשְׁתַּנֶּה יֵשׁ צִיר; לַמַּעֲרֶכֶת יֵשׁ אֵין־סוֹף פִּתְרוֹנוֹת.",
    "system.empty": "לֹא סֻפְּקוּ מִשְׁוָאוֹת.",
    "substitution_intro": "מַצִּיבִים אֶת הָעֲרָכִים: {substitutions}.",
    "derivative_result": "יֻשְּׂמוּ כְּלָלֵי הַגְּזִירָה.",
    "minus_one_power_parity": "$-1^{{{exponent}}}$ תָּלוּי בַּזּוּגִיּוּת; הַתּוֹצָאָה הִיא ${result}$.",
    "addition_borrow_suffix": ", לָכֵן נִלְוֶה {-carry} מֵהָעַמּוּדָה הַבָּאָה וְנִכְתֹּב {digit} כָּאן.",
    "addition_carry_row": "$10^{{{p+1}}}$: {carry} (נֶשֶׂא מֵהָעַמּוּדָה הַקּוֹדֶמֶת)",
    "addition_carry_suffix": ", לָכֵן נִשָּׂא {carry} לָעַמּוּדָה הַבָּאָה.",
    "addition_decompose_intro": "נְפָרֵק אֶת ${a}$ וְ-${b}$ לְרְכִיבִים לְפִי עֶרֶךְ מָקוֹם.",
    "addition_put_together": "נְחַבֵּר אֶת עַמּוּדוֹת עֶרֶךְ הַמָּקוֹם כְּדֵי לְקַבֵּל ${result}$.",
    "multiply_approximate_a": "נְקָרֵב אֶת ${a}$ ל-${a_approx}$ כְּדֵי לִשְׁלֹט בְּדִיּוּק בֵּינַיִם בְּמַהֲלָךְ הַכֶּפֶל.",
    "multiply_approximate_b": "נְקָרֵב אֶת ${b}$ ל-${b_approx}$ כְּדֵי לִשְׁלֹט בְּדִיּוּק בֵּינַיִם בְּמַהֲלָךְ הַכֶּפֶל.",
    "multiply_complex_intro": "נְחַשֵּׁב אֶת ${a} \\cdot {b}$ בְּאֶמְצָעוּת פֵּרוּק לְפִי עֶרֶךְ מָקוֹם: נִיצּוֹר מַכְפֵּלוֹת חֶלְקִיּוֹת, וְאָז נְחַבֵּר אוֹתָן.",
    "multiply_decimal_shift_a": "נִכְתֹּב מֵחָדָשׁ אֶת ${a}$ כְּעֶרֶךְ שָׁלֵם מוּכְפָּל בְּ-$10^{{{a_exponent}}}$.",
    "multiply_decimal_shift_b": "נִכְתֹּב מֵחָדָשׁ אֶת ${b}$ כְּעֶרֶךְ שָׁלֵם מוּכְפָּל בְּ-$10^{{{b_exponent}}}$.",
    "multiply_table_header": "\n**טַבְלַת מַכְפֵּלוֹת חֶלְקִיּוֹת:**",
    "multiply_values_list_header": "**נְחַבֵּר אֶת הָעֲרָכִים הַחֶלְקִיִּים הָאֵלֶּה לְפִי עֶרֶךְ מָקוֹם:**",
    "overflow_infinity": "${previous}$ חוֹרֵג מִגְּבוּל הַמַּעֲרִיךְ הַמּוּגְדָּר, לָכֵן נְקָרֵב אוֹתוֹ ל-$\\infty$.",
    "overflow_python_infinity": "${previous}$ גָּרַם לַחֲרִיגָה (overflow) בְּמַהֲלָךְ הַחִשּׁוּב הַמִּסְפָּרִי, לָכֵן נְקָרֵב אוֹתוֹ ל-$\\infty$.",
    "overflow_python_symbolic": "${render_latex(expression)}$ גָּרַם לַחֲרִיגָה (overflow) בְּמַהֲלָךְ הַחִשּׁוּב הַמִּסְפָּרִי, לָכֵן נַשְׁאִיר אוֹתוֹ בְּצוּרָה סִימְבּוֹלִית.",
    "overflow_python_zero": "${previous}$ גָּרַם לַחֲרִיגָה (overflow) בְּמַהֲלָךְ הַחִשּׁוּב הַמִּסְפָּרִי, לָכֵן נְקָרֵב אוֹתוֹ ל-$0$.",
    "overflow_symbolic": "${render_latex(expression)}$ חוֹרֵג מִגְּבוּל הַמַּעֲרִיךְ הַמִּסְפָּרִי הַמּוּגְדָּר, לָכֵן נַשְׁאִיר אוֹתוֹ בְּצוּרָה סִימְבּוֹלִית.",
    "overflow_zero": "${previous}$ חוֹרֵג מִגְּבוּל הַמַּעֲרִיךְ הַמּוּגְדָּר, לָכֵן נְקָרֵב אוֹתוֹ ל-$0$.",
    "zero_power_negative": "0 בְּחֶזְקָה שְׁלִילִית אֵינוֹ מוּגְדָּר.",
    "zero_power_positive": "0 בְּחֶזְקָה חִיּוּבִית הוּא 0.",
    "zero_power_symbolic": "נַשְׁאִיר אֶת ${render_latex(symbolic_zero_power)}$ סִימְבּוֹלִי כִּי סִימַן הַמַּעֲרִיךְ אֵינוֹ יָדוּעַ.",
    "zero_power_zero_one": "$0^0$ מוּגְדָּר לְהִתְחַשֵּׁב כְּ-$1$.",
    "zero_power_zero_undefined": "0^0 אֵינוֹ מוּגְדָּר בְּתַצּוּרַת מַעֲרִיךְ זוֹ.",
    "zero_power_zero_zero": "$0^0$ מוּגְדָּר לְהִתְחַשֵּׁב כְּ-$0$.",
    "base_trivial_power": "1 בְּכָל חֶזְקָה הוּא 1.",
    "domain_error_function": "עֲצֹר כָּאן: ${render_latex(e.expression)}$ אֵינוֹ מוּגְדָּר עֲבוּר {e.expression.function.name}, לָכֵן הַבִּיטּוּי מִחוּץ לַתְּחוּם שֶׁלּוֹ.",
    "domain_error_generic": "עֲצֹר כָּאן: ${render_latex(e.expression)}$ אֵינוֹ מוּגְדָּר בִּתְחוּם הַמִּסְפָּרִים הַמַּמָּשִׁיִּים שֶׁבְּשִׁמּוּשׁ הַמַּעֲרִיךְ הַזֶּה.",
    "integral_definite_result": "יִשּׂוּם הַמִּשְׁפָּט הַיְּסוֹדִי שֶׁל הַחֶדְוָ\"א: חִשּׁוּב הַקְּדוּמָה בַּגְּבוּלוֹת וְחִסּוּר, $F({render_latex(upper)}) - F({render_latex(lower)})$.",
    "integral_indefinite_result": "חִשּׁוּב פּוּנְקְצִיָּה קְדוּמָה לְפִי ${expression.variable.name}$.",
}


_LOCALE_OVERRIDES: dict[str, dict[str, str]] = {
    "en": {},
    "es": _ES_MESSAGES,
    "fr": _FR_MESSAGES,
    "de": _DE_MESSAGES,
    "ko": _KO_MESSAGES,
    "he": _HE_MESSAGES,
    "he-niqqud": _HE_NIQQUD_MESSAGES,
}


_STYLE_OVERRIDES: dict[str, dict[str, str]] = {
    "default": {},
    "compact": {
        "render.step.block": "{body}",
        "render.single_step.block": "{body}",
        "render.step.joiner": "\n",
    },
    "plain": {
        "step.heading": "Step {number}",
        "render.step.block": "{heading}: {body}",
        "render.single_step.block": "{body}",
    },
    "xml": {
        "render.document.prefix": "<steps>\n",
        "render.document.suffix": "\n</steps>",
        "render.step.block": "<step index=\"{number}\">\n<heading>{heading}</heading>\n<body>{body}</body>\n</step>",
        "render.single_step.block": "<step index=\"{number}\">\n<body>{body}</body>\n</step>",
        "render.step.joiner": "\n",
    },
}

_INTENTIONALLY_SHARED_KEYS: set[str] = {
    # Language-neutral math-form fallback.
    "calculator.fallback",
    # Comma-separated list formatting is intentionally shared.
    "substitution.separator_many",
    # Newline joiners are structural and language-neutral.
    "render.step.joiner",
    "render.substep.joiner",
    # "Solution" is valid unchanged label in several locales.
    "equation_manual_review.solution",
}


def get_builtin_messages(locale: str, style_type: StyleType = "default") -> dict[str, str]:
    normalized_locale = (locale or "en").lower()
    resolved_locale = normalized_locale if normalized_locale in _LOCALE_OVERRIDES else "en"
    resolved_style = style_type if style_type in _STYLE_OVERRIDES else "default"
    merged = dict(_EN_MESSAGES)
    merged.update(_LOCALE_OVERRIDES[resolved_locale])
    merged.update(_STYLE_OVERRIDES[resolved_style])
    return merged


def supported_locales() -> list[str]:
    return sorted(_LOCALE_OVERRIDES.keys())


def supported_style_types() -> list[str]:
    return sorted(_STYLE_OVERRIDES.keys())


_placeholder_pattern = re.compile(r"\{([a-zA-Z_][a-zA-Z0-9_]*)\}")


def validate_pack_placeholders(locale: str) -> list[str]:
    errors: list[str] = []
    overrides = _LOCALE_OVERRIDES.get(locale, {})
    for key, localized in overrides.items():
        base = _EN_MESSAGES.get(key)
        if base is None:
            continue
        expected = set(_placeholder_pattern.findall(base))
        actual = set(_placeholder_pattern.findall(localized))
        if expected != actual:
            errors.append(
                f"{locale}:{key}: expected placeholders {sorted(expected)}, got {sorted(actual)}"
            )
    return errors


def locale_equal_to_english_keys(locale: str) -> list[str]:
    if locale == "en":
        return []
    merged = get_builtin_messages(locale, "default")
    return sorted(
        k
        for k, v in _EN_MESSAGES.items()
        if merged.get(k) == v and k not in _INTENTIONALLY_SHARED_KEYS
    )
