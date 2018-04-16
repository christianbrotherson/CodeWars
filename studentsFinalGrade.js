// initial implementation
const finalGrade = (exam, projects) => {
    if (exam > 90 || projects > 10) {
        return 100
    } else if (exam > 75 && projects >= 5) {
        return 90
    } else if (exam > 50 && projects >= 2) {
        return 75
    } else {
        return 0
    }
}

// refacored implementation
const finalGradeRefactor = (exam, projects) => exam > 90 || projects > 10 ? 100 : exam > 75 && projects > 4 ? 90 : exam > 50 && projects > 1 ? 75 : 0;