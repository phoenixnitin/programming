// Fundfina

// 1 1 1 1 1
// 0 1 0 0 1
// 0 1 1 0 1
// 0 0 1 0 1
// 0 0 1 0 0 

function initialize_visited(m, n) {

}

function find_path(matrix, m, n) {
    visited = initialize_visited(m, n);
    found = explore(matrix, 0, 0, visited, m, n);

}

function explore(matrix, i, j, visited, m, n, dest_i, dest_j) {
    if(i == dest_i && j == dest_j && matrix[i][j]) {
        console.log(dest_i, dest_j);
        return true;
    };
    
    value = false;
    if(i>=0 && i<=m && j>=0 && j<=n && !visited[i][j] && matrix[i][j]) {
        visited[i][j] = 1;
        value = explore(matrix, i + 1, j, visited, m, n, dest_i, dest_j);
        value = value || explore(matrix, i - 1, j, visited, m, n, dest_i, dest_j);
        value = value || explore(matrix, i, j + 1, visited, m, n, dest_i, dest_j);
        value = value || explore(matrix, i, j - 1, visited, m, n, dest_i, dest_j);
        if (value) {
            console.log(i,j);
        }
    }
    return value;
}