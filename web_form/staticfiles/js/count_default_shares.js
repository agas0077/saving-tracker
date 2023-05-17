const YEARS = [
    2020, 2021, 2022, 2023, 2024, 2025, 2026, 2027
];
const yearInputs = YEARS.map(currentYear => {return `id_share_${currentYear}`} );
const sourceInputs = ['id_primary_share', 'id_secondary_share', 'id_warehouse_share']
const functionInputs = ['id_personal_care_share', 'id_home_care_share', 'id_tea_share', 'id_ic_share', 'id_food_share',]

window.onload = roundValuesInit

document.addEventListener('click', (event) => {
    console.log(event)
    if (event.target.id === 'default_btn') {
        defaultSplitInit();
    }
});

let lastEventTargetId = ''
document.addEventListener('keyup', (event) => {
    console.log(event)
    if (yearInputs.includes(event.target.id)) {
        enteredValueSplit(event.target.id);
    }
    if (sourceInputs.includes(event.target.id)) {
        enteredValueSplit(event.target.id);
    }
    if (functionInputs.includes(event.target.id)) {
        enteredValueSplit(event.target.id);
    }
});

function defaultSplitCount(currentYear, ds, de, savingPerDay, saving) {

    const yearStart = ds.getUTCFullYear();
    const yearEnd = de.getUTCFullYear();
    let newValue = 0
    if (currentYear > yearStart && currentYear < yearEnd) {
        const s = new Date(currentYear, 0, 1)  // 0 - Январь, 11 - Декабрь
        const e = new Date(currentYear, 11, 31)  // 0 - Январь, 11 - Декабрь
        const diffTime = Math.abs(e - s);
        const diffDays = Math.ceil(diffTime / (1000 * 60 * 60 * 24));
        newValue = savingPerDay * diffDays;
    }
    if (currentYear < yearStart || currentYear > yearEnd) {
        newValue = 0;
    }
    if (currentYear == yearStart) {
        const e = new Date(currentYear, 11, 31)  // 0 - Январь, 11 - Декабрь
        const diffTime = Math.abs(e - ds);
        const diffDays = Math.ceil(diffTime / (1000 * 60 * 60 * 24));
        newValue = savingPerDay * diffDays;
    }
    if (currentYear == yearEnd) {
        const s = new Date(currentYear, 0, 1)  // 0 - Январь, 11 - Декабрь
        const diffTime = Math.abs(de - s);
        const diffDays = Math.ceil(diffTime / (1000 * 60 * 60 * 24));
        newValue = savingPerDay * diffDays;
    }
    if (currentYear == yearStart && currentYear == yearEnd) {
        const diffTime = Math.abs(de - ds);
        const diffDays = Math.ceil(diffTime / (1000 * 60 * 60 * 24));
        newValue = savingPerDay * diffDays;
    }

    const persantage = newValue / saving;

    document.getElementById(`id_share_${currentYear}`).value = Math.round(persantage * 100) / 100;
    document.getElementById(`id_share_${currentYear}_cell`).textContent = Math.round(newValue * 100) / 100;
}

function defaultSplitInit() {
    const dateStart = new Date(document.getElementById('id_initial_start_date').value);
    const dateEnd = new Date(document.getElementById('id_project_end_date').value);
    const saving = document.getElementById('id_saving_potential').value;
    const diffTime = Math.abs(dateEnd - dateStart);
    const diffDays = Math.ceil(diffTime / (1000 * 60 * 60 * 24));

    const savingPerDay = saving / diffDays;

    YEARS.map(currentYear => defaultSplitCount(currentYear, dateStart, dateEnd, savingPerDay, saving));
}

function enteredValueSplit(id) {
    persantage = document.getElementById(id).value;
    const saving = document.getElementById('id_saving_potential').value;
    document.getElementById(`${id}_cell`).textContent = Math.round(saving * persantage * 100) / 100;
}

function roundValuesInit() {
    yearInputs.forEach(input => {
        const content = document.getElementById(`${input}_cell`).textContent;
        const float = parseFloat(content.replace(",", "."))
        document.getElementById(`${input}_cell`).textContent = Math.round(float * 100) / 100;
    });
}