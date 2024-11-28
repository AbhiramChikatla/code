#include <stdio.h>

int main() {
    int p[10], at[10], bt[10], ct[10], tat[10], wt[10], i, j, temp = 0, n;
    float awt = 0, atat = 0;

    printf("Enter number of processes you want: ");
    scanf("%d", &n);

    printf("Enter %d process IDs: ", n);
    for (i = 0; i < n; i++) {
        scanf("%d", &p[i]);
    }

    printf("Enter %d arrival times: ", n);
    for (i = 0; i < n; i++) {
        scanf("%d", &at[i]);
    }

    printf("Enter %d burst times: ", n);
    for (i = 0; i < n; i++) {
        scanf("%d", &bt[i]);
    }

    // Sorting processes based on arrival time
    for (i = 0; i < n - 1; i++) {
        for (j = 0; j < n - i - 1; j++) {
            if (at[j] > at[j + 1]) {
                // Swap process IDs
                temp = p[j + 1];
                p[j + 1] = p[j];
                p[j] = temp;

                // Swap arrival times
                temp = at[j + 1];
                at[j + 1] = at[j];
                at[j] = temp;

                // Swap burst times
                temp = bt[j + 1];
                bt[j + 1] = bt[j];
                bt[j] = temp;
            }
        }
    }

    // Calculating completion times
    ct[0] = at[0] + bt[0];
    for (i = 1; i < n; i++) {
        temp = 0;
        if (ct[i - 1] < at[i]) {
            temp = at[i] - ct[i - 1];
        }
        ct[i] = ct[i - 1] + bt[i] + temp;
    }

    printf("\nP\tA.T\tB.T\tC.T\tTAT\tWT");
    for (i = 0; i < n; i++) {
        tat[i] = ct[i] - at[i]; // Turnaround time
        wt[i] = tat[i] - bt[i]; // Waiting time
        atat += tat[i];
        awt += wt[i];
        printf("\nP%d\t%d\t%d\t%d\t%d\t%d", p[i], at[i], bt[i], ct[i], tat[i], wt[i]);
    }

    // Average turnaround time and waiting time
    atat = atat / n;
    awt = awt / n;

    printf("\nAverage Turnaround Time: %.2f", atat);
    printf("\nAverage Waiting Time: %.2f\n", awt);

    return 0;
}
