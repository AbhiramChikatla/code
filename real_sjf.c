#include <stdio.h>

int main() {
    int bt[20], p[20], wt[20], tat[20], i, j, n, total = 0, pos, temp;
    float avg_wt, avg_tat;

    printf("Enter number of processes: ");
    scanf("%d", &n);

    printf("\nEnter Burst Time:\n");
    for (i = 0; i < n; i++) {
        printf("P%d: ", i + 1);
        scanf("%d", &bt[i]);
        p[i] = i + 1; // Save process ID
    }

    // Sorting burst times and process IDs in ascending order using selection sort
    for (i = 0; i < n; i++) {
        pos = i;
        for (j = i + 1; j < n; j++) {
            if (bt[j] < bt[pos]) {
                pos = j;
            }
        }

        // Swap burst times
        temp = bt[i];
        bt[i] = bt[pos];
        bt[pos] = temp;

        // Swap process IDs
        temp = p[i];
        p[i] = p[pos];
        p[pos] = temp;
    }

    // Calculating waiting time
    wt[0] = 0; // Waiting time for first process is 0
    for (i = 1; i < n; i++) {
        wt[i] = 0;
        for (j = 0; j < i; j++) {
            wt[i] += bt[j];
        }
        total += wt[i]; // Accumulate total waiting time
    }

    avg_wt = (float) total / n; // Average waiting time
    total = 0;

    printf("\nProcess\tBurst Time\tWaiting Time\tTurnaround Time");
    for (i = 0; i < n; i++) {
        tat[i] = bt[i] + wt[i]; // Turnaround time = burst time + waiting time
        total += tat[i]; // Accumulate total turnaround time
        printf("\nP%d\t\t%d\t\t%d\t\t%d", p[i], bt[i], wt[i], tat[i]);
    }

    avg_tat = (float) total / n; // Average turnaround time

    printf("\n\nAverage Waiting Time = %.2f", avg_wt);
    printf("\nAverage Turnaround Time = %.2f\n", avg_tat);

    return 0;
}
