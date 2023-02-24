const getCookie = (name) => {
    if (document.cookie && document.cookie !== '') {
        for (const cookie of document.cookie.split(';')) {
            const [key, value] = cookie.trim().split('=');
            if (key === name) {
                return decodeURIComponent(value);
            }
        }
    }
};
const csrftoken = getCookie('csrftoken');


// ②選択されたセレクトメニュー情報をDjango側にPOST送信してデータを取得する
// セレクトメニュー内の要素を取得する
const weapon = document.getElementById('weapon_select');
console.log(weapon);
// セレクトメニューの値が変更された時に実行される処理
weapon.addEventListener('change', (event) => {
    // セレクトメニュー内で選択された値の順番を取得する
    const selectedWeaponId = weapon.selectedIndex;
    const selectedWeapon = weapon[selectedWeaponId].id;
    // 非同期処理を記述する
    async function memory_list() {
        const url = '/top_info';
        let res = await fetch(url, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/x-www-form-urlencoded; charset=utf-8',
                    'X-CSRFToken': csrftoken,
                },
                body: `weapon=${selectedWeapon}`
            });
            let json = await res.json();
            let memory_list = json.memory_list;
            let table = document.getElementById('memory-container');
            table.innerHTML = '';
            for (let memory of memory_list) {
                let tr = table.insertRow();
                let td = tr.insertCell();
                let text = document.createTextNode(`${memory.xp}`);
                td.appendChild(text);
                td = tr.insertCell();
                let atag = document.createElement("a");
                atag.href = `/memories/${memory.id}/`;
                atag.innerText = `${memory.title}`
                td.appendChild(atag);
                td = tr.insertCell();
                text = document.createTextNode(`${memory.weapon}`)
                td.appendChild(text);
                td = tr.insertCell();
                text = document.createTextNode(`${memory.stage}`);
                td.appendChild(text);
                td = tr.insertCell();
                text = document.createTextNode(`${memory.rule}`);
                td.appendChild(text);
            }
        }
    // 定義した関数を実行する
    memory_list();
})

/*
const stage = document.getElementById('stage_select');
stage.addEventListener('change', (event) => {
    // セレクトメニュー内で選択された値の順番を取得する
    const selectedStageId = stage.selectedIndex;
    const selectedStage = stage[selectedStageId].id;
    // 非同期処理を記述する
    async function memory_list_stage() {
        const url = '/top_info';
        let res = await fetch(url, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/x-www-form-urlencoded; charset=utf-8',
                    'X-CSRFToken': csrftoken,
                },
                body: `stage=${selectedStage}`
            });
            let json = await res.json();
            let memory_list = json.memory_list;
            let table = document.getElementById('memory-container');
            table.innerHTML = '';
            for (let memory of memory_list) {
                let tr = table.insertRow();
                let td = tr.insertCell();
                let text = document.createTextNode(`${memory.xp}`);
                td.appendChild(text);
                td = tr.insertCell();
                let atag = document.createElement("a");
                atag.href = `/memories/${memory.id}/`;
                atag.innerText = `${memory.title}`
                td.appendChild(atag);
                td = tr.insertCell();
                text = document.createTextNode(`${memory.weapon}`)
                td.appendChild(text);
                td = tr.insertCell();
                text = document.createTextNode(`${memory.stage}`);
                td.appendChild(text);
                td = tr.insertCell();
                text = document.createTextNode(`${memory.rule}`);
                td.appendChild(text);
            }
        }
    // 定義した関数を実行する
    memory_list_stage();
})*/
