let currentSource = 'topuniversities';
let currentData = [];

async function getEntriesTopUniversities() {
    const url = `/api/qs_universities/?items_per_page=1000`; // Fetch all items

    try {
        const response = await fetch(url);
        const data = await response.json();

        if (!data.data) throw new Error("No data found");

        return data.data.map(entry => ({
            rank: entry.rank,
            name: entry.title,
            overall_score: entry.overall_score
        }));
    } catch (error) {
        console.error('Error fetching Top Universities data:', error);
        throw error;
    }
}

async function getEntriesTimesHigherEducation() {
    const url = `/api/the_universities/?items_per_page=1000`; // Fetch all items

    try {
        const response = await fetch(url);
        const data = await response.json();

        if (!data.data) throw new Error("No data found");

        return data.data.map(entry => ({
            rank: entry.rank,
            name: entry.name,
            overall_score: entry.scores_overall,
        }));
    } catch (error) {
        console.error('Error fetching data from your API:', error);
        throw error;
    }
}

async function displayEntries() {
    document.getElementById('loadingSpinner').style.display = 'block';

    try {
        let data;
        if (currentSource === 'topuniversities') {
            data = await getEntriesTopUniversities();
        } else if (currentSource === 'timeshighereducation') {
            data = await getEntriesTimesHigherEducation();
        }
        currentData = { entries: data };
        displayEntriesList();
    } catch (error) {
        console.error('Error fetching data:', error);
    } finally {
        document.getElementById('loadingSpinner').style.display = 'none';
    }
}

function displayEntriesList() {
    const tbody = document.querySelector('#unisTable tbody');
    tbody.innerHTML = '';

    const actualRanking = document.querySelector('#actualRanking');
    actualRanking.innerHTML = currentSource === 'topuniversities' ? 'Rank by QS' : 'Rank by THE';

    let r = 0;
    currentData.entries.forEach(entry => {
        r++;
        const row = document.createElement('tr');
        row.innerHTML = `
            <td>${r}</td>
            <td>${entry.name}
                <div class="details-button-container">
                    <button class="btn btn-info" onclick="redirectToUniversityPage('${entry.name}')">Details</button>
                </div>
            </td>
            <td>${entry.rank}</td>
            <td>${entry.overall_score}</td>
        `;
        tbody.appendChild(row);
    });
}

function switchSource(source) {
    currentSource = source;
    displayEntries();  // Fetch and display the rankings directly based on source
}

async function instantSearch() {
    const searchTerm = document.getElementById('searchBar').value.trim().toLowerCase();
    const tbody = document.querySelector('#unisTable tbody');
    tbody.innerHTML = '';

    if (searchTerm === '') {
        displayEntriesList(); // Display all data if search term is empty
        return;
    }

    const searchResults = currentData.entries.filter(entry => entry.name.toLowerCase().includes(searchTerm));

    if (searchResults.length > 0) {
        let r = 0;
        searchResults.forEach(entry => {
            r++;
            const row = document.createElement('tr');
            row.innerHTML = `
                <td>${r}</td>
                <td>${entry.name}
                    <div class="details-button-container">
                        <button class="btn btn-info" onclick="redirectToUniversityPage('${entry.name}')">Details</button>
                    </div>
                </td>
                <td>${entry.rank}</td>
                <td>${entry.overall_score}</td>
            `;
            tbody.appendChild(row);
        });
    } else {
        const noResultsRow = document.createElement('tr');
        noResultsRow.innerHTML = `<td colspan="4">No results found for "${searchTerm}".</td>`;
        tbody.appendChild(noResultsRow);
    }
}

function redirectToUniversityPage(uni) {
    let formattedUni;

    const abbreviationMatch = uni.match(/\(([^)]+)\)$/);
    if (abbreviationMatch) {
        formattedUni = abbreviationMatch[1].toLowerCase();
    } else {
        formattedUni = uni.toLowerCase()
            .replace(/\s+/g, '-')  
            .replace(/[()]/g, '')  
            .replace(/,/g, '')     
            .replace(/-+$/, '');   
    }

    window.location.href = `/unipage/${formattedUni}`;
}

document.addEventListener('DOMContentLoaded', function() {
    displayEntries();  // Display the initial ranking by default
});
