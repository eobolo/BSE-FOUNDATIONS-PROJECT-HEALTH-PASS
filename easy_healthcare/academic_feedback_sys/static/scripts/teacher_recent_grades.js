const inputSearch = document.querySelector(".input-search");
inputSearch.addEventListener("input", (e) => {
    let value = e.target.value;
    const tableBodyFilter = document.querySelector(".filter");
    const tableBodyOriginal = document.querySelector(".original");
    let allBodyRowsFilter = tableBodyOriginal.querySelectorAll("tr");
    // clone the original tr rows before filtering
    allBodyRowsFilter = Array.from(allBodyRowsFilter)
    allBodyRowsFilter = allBodyRowsFilter.map((eachBodyRow) => eachBodyRow.cloneNode(true));
    const handleId = (eachBodyRow) => {
        // search using data-id class
        const idTableData = eachBodyRow.querySelector('.data-id');
        if (((idTableData.textContent).toLowerCase()).includes((value.toLowerCase()))) {
            return true;
        } else {
            return false;
        }
    }
    const handleFirstName = (eachBodyRow) => {
        // search using first_name class
        const firstNameDataTable = eachBodyRow.querySelector('.first_name');

        if (((firstNameDataTable.textContent).toLowerCase()).includes((value.toLowerCase()))) {
            return true;
        } else {
            return false;
        }
    }
    const handleLastName = (eachBodyRow) => {
        // search using last_name class
        const lastNameDataTable = eachBodyRow.querySelector('.last_name');

        if (((lastNameDataTable.textContent).toLowerCase()).includes((value.toLowerCase()))) {
            return true;
        } else {
            return false;
        }
    }
    const handleMiddleName = (eachBodyRow) => {
        // search using middle_name class
        const middleNameDataTable = eachBodyRow.querySelector('.middle_name');

        if (((middleNameDataTable.textContent).toLowerCase()).includes((value.toLowerCase()))) {
            return true;
        } else {
            return false;
        }
    }
    const handleClassLevel = (eachBodyRow) => {
        // search using class_level class
        const classLevelDataTable = eachBodyRow.querySelector('.class_level');

        if (((classLevelDataTable.textContent).toLowerCase()).includes((value.toLowerCase()))) {
            return true;
        } else {
            return false;
        }
    }
    const handleSemester = (eachBodyRow) => {
        // search using semester class
        const semesterDataTable = eachBodyRow.querySelector('.semester');

        if (((semesterDataTable.textContent).toLowerCase()).includes((value.toLowerCase()))) {
            return true;
        } else {
            return false;
        }
    }
    const handleYear = (eachBodyRow) => {
        // search using first_name class
        const yearDataTable = eachBodyRow.querySelector('.year');

        if (((yearDataTable.textContent).toLowerCase()).includes((value.toLowerCase()))) {
            return true;
        } else {
            return false;
        }
    }
    let filteredRows = allBodyRowsFilter.filter((eachBodyRow) => (handleId(eachBodyRow)) || (handleFirstName(eachBodyRow)) || (handleLastName(eachBodyRow)) || handleMiddleName(eachBodyRow) || handleClassLevel(eachBodyRow) || handleSemester(eachBodyRow) || handleYear(eachBodyRow));
    tableBodyFilter.replaceChildren(...filteredRows);
})