{% autoescape off %}
const total_questions = {{ article.total_questions }}; // ユーザに解かせる問題数
var jsonData = JSON.stringify({{ article.body }});
console.log(jsonData);
var data = JSON.parse(jsonData);
console.log(data);
const questions = random(data, total_questions);
console.log(questions);
let question_number = 1; // 問題番号
let q = questions[question_number - 1]; // 抽出したquestionsを先頭から表示していく(一つのqはquestion, select1, select2, select3, select4, correctを要素に持つ)
let question = q["question"];
let select1 = q["select1"];
let select2 = q["select2"];
let select3 = q["select3"];
let select4 = q["select4"];
let correct = q["correct"]; // correctは整数
{% endautoescape %}
let ratio;
let num_correct = 0;


// article.bodyからtotal_questionsの数だけランダムに抽出
function random(array, num) {
    var a = array;
    var t = [];
    var questions = [];
    var l = a.length;
    var n = num < l ? num : l;
    while (n-- > 0) {
        var i = (Math.random() * l) | 0;
        questions[n] = t[i] || a[i];
        --l;
        t[i] = t[l] || a[l];
    }
    return questions; // 抽出された要素がquestionsに格納される
}

// もう一度挑戦する
function reflesh() {
    window.location.reload();
}
// 前のページに戻る
function last() {
    window.history.back();
}

// 結果を見る
function result_access() {
    window.location.href = "{% url 'result' article.id %}";
}


// 正誤判定(nはselectの番号)
function discri_answer(n) {
    column = document.getElementById("output");
    if (correct == n && total_questions != question_number) {
        column.innerHTML = "<strong><font size='5' color='#ff0000'>選択肢[" + correct + "] 正解！！</font></strong> <input id='next_but' type='button' value='クリックして次へ進もう' onclick='next();'/><br><br>";
        num_correct++;
        columnq = document.getElementById("num_correct");
        columnq.innerHTML = num_correct;
    } else if (correct != n && total_questions != question_number) {
        column.innerHTML = "<strong><font size='5' color='#0000ff'>残念！！正解は[" + correct + "]</font></strong> <input id='next_but' type='button' value='クリックして次へ進もう' onclick='next();'/><br><br>";
    } else if (correct == n && total_questions == question_number) {
        num_correct++;
        ratio = num_correct / question_number * 100;
        ratio = ratio.toFixed();
        time = (Date.now() - time) / 1000;
        compliment = "";
        if (ratio <= 25) {
            compliment = "<font color='#000077' size='10'><i>try hard ...</i></font>";
        } else if (ratio > 25 && ratio <= 70) {
            compliment = "<font color='#005500' size='10'><i>way to go</i></font>";
        } else if (ratio > 70 && ratio <= 99) {
            compliment = "<font color='#ff4500' size='10'><i>*better luck next time*</i></font>";
        } else if (ratio > 99) {
            compliment = "<font color='#880000' size='10'><i>excellent!!</i></font>";
        } else {
            compliment = "さらに研鑽を積もう";
        }
        column.innerHTML = "<strong><font size='5' color='#ff0000'>選択肢[" + correct + "] 正解！！</font> <font size='5'>全問終了!!お疲れさまでした。</font></strong><br><br><font size='5'>かかった時間は<strong>" + time + "秒</strong> 正答率は" + num_correct + "/" + question_number + "=<strong>" + ratio + "%</strong>でした</font><br><br><strong>" + compliment + "</strong><br><br><input id='next_but' type='button' value='もう一度挑戦する' onclick='reflesh();'/><br><br><input id='next_but' type='button' value='前のページに戻る' onclick='last();'/><br><br><input id='next_but' type='button' value='結果を見る' onclick='result_access();'/><br><br>";
        columnq = document.getElementById("num_correct");
        columnq.innerHTML = num_correct;
    } else if (correct != n && total_questions == question_number) {
        ratio = num_correct / question_number * 100;
        ratio = ratio.toFixed(2)
        time = (Date.now() - time) / 1000;
        compliment = "";
        if (ratio <= 25) {
            compliment = "<font color='#000077' size='10'><i>try hard ...</i></font>";
        } else if (ratio > 25 && ratio <= 70) {
            compliment = "<font color='#005500' size='10'><i>way to go</i></font>";
        } else if (ratio > 70 && ratio <= 99) {
            compliment = "<font color='#ff4500' size='10'><i>*better luck next time*</i></font>";
        } else if (ratio > 99) {
            compliment = "<font color='#880000' size='10'><i>excellent!!</i></font>";
        } else {
            compliment = "さらに研鑽を積もう";
        }
        column.innerHTML = "<strong><font size='5' color='#0000ff'>残念！！正解は[" + correct + "]</font> <font size='5'>全問終了!!お疲れさまでした。</font></strong><br><br><font size='5'>かかった時間は<strong>" + time + "秒</strong> 正答率は" + num_correct + "/" + question_number + "=<strong>" + ratio + "%</strong>でした</font><br><br><strong>" + compliment + "</strong><br><br><input id='next_but' type='button' value='もう一度挑戦する' onclick='reflesh();'/><br><br><input id='next_but' type='button' value='前のページに戻る' onclick='last();'/><br><br><input id='next_but' type='button' value='結果を見る' onclick='result_access();'/><br><br>";
    }
    document.getElementById("but1").disabled = true;
    document.getElementById("but2").disabled = true;
    document.getElementById("but3").disabled = true;
    document.getElementById("but4").disabled = true;
}

// 次へ進む
function next() {
    question_number++;
    q = questions[question_number - 1]; // 抽出したquestionsを先頭から表示していく(一つのqはquestion, select1, select2, select3, select4, correctを要素に持つ)
    question = q["question"];
    select1 = q["select1"];
    select2 = q["select2"];
    select3 = q["select3"];
    select4 = q["select4"];
    correct = q["correct"]; // correctは整数
    console.log(q);
    console.log(correct);
    column = document.getElementById("output");
    column.innerHTML = "";
    document.getElementById("but1").disabled = false;
    document.getElementById("but2").disabled = false;
    document.getElementById("but3").disabled = false;
    document.getElementById("but4").disabled = false;
    columnq = document.getElementById("question_number");
    columnq.innerHTML = question_number;
    columnq = document.getElementById("quest");
    columnq.innerHTML = question;
    column1 = document.getElementById("but1");
    column1.value = "[1] " + select1;
    column2 = document.getElementById("but2");
    column2.value = "[2] " + select2;
    column3 = document.getElementById("but3");
    column3.value = "[3] " + select3;
    column4 = document.getElementById("but4");
    column4.value = "[4] " + select4;
}

document.open();
document.write(total_questions + "問中 <span id='question_number'>" + question_number + "</span>問目 正解数<span id='num_correct'>" + num_correct + "</span>");
document.write("<p><div id='quest' style='font-size:25px;'>" + question + " 選択肢をクリックしてください</div></p><br>");
document.write("<div id='output'></div>");
document.write("<input id='but1' type='button' style='text-align: left; width:30%;font-size:20px;' value=[1]" + select1 + " onclick='discri_answer(1);'/><br><br>");
document.write("<input id='but2' type='button' style='text-align: left; width:30%;font-size:20px;' value=[2]" + select2 + " onclick='discri_answer(2);'/><br><br>");
document.write("<input id='but3' type='button' style='text-align: left; width:30%;font-size:20px;' value=[3]" + select3 + " onclick='discri_answer(3);'/><br><br>");
document.write("<input id='but4' type='button' style='text-align: left; width:30%;font-size:20px;' value=[4]" + select4 + " onclick='discri_answer(4);'/><br><br>");
document.close();
time = Date.now();