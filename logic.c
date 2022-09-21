#include <stdlib.h>
#include <stdio.h>
#include <string.h>
#include <stdbool.h>

/**
 * Auto-generated code below aims at helping you parse
 * the standard input according to the problem statement.
 **/

int main()
{
    int n;
    scanf("%d", &n);
    int m;
    scanf("%d", &m);
    int signal_len;
    char signal_names[4][9]; // Array of input names
    int signals[4][65]; // Array of input signals
    for (int i = 0; i < n; i++) {
        char input_name[9];
        char input_signal[65];
        scanf("%s%s", input_name, input_signal);
        signal_len = strlen(input_signal);

        // Add strings to arrays
        strcpy(signal_names[i], input_name);

        // Convert stripes to numbers
        int input_signal_n[signal_len];
        for (int j = 0; j < signal_len; j++) {
            if (input_signal[j] == '-') {
                signals[i][j] = 1;
            } else {
                signals[i][j] = 0;
            }
        }
    }
    for (int i = 0; i < m; i++) {
        char output_name[9];
        char type[9];
        char input_name_1[9];
        char input_name_2[9];
        scanf("%s%s%s%s", output_name, type, input_name_1, input_name_2);

        // Get index of the input_names
        int index_1, index_2;
        for (int j = 0; j < n; j++) {
            if (strcmp(input_name_1, signal_names[j]) == 0) {
                index_1 = j;
            }
            if (strcmp(input_name_2, signal_names[j]) == 0) {
                index_2 = j;
            }
        }

        // Calculate output signal
        char output_signal[signal_len];

        // Loop through signal
        for (int j = 0; j < signal_len; j++) {
            char signal;
            if (strcmp(type, "AND") == 0) {
                if (signals[index_1][j] + signals[index_2][j] == 2){
                    signal = '-';
                } else {
                    signal = '_';
                }
            } else if (strcmp(type, "OR") == 0) {
                if (signals[index_1][j] + signals[index_2][j] >= 1){
                    signal = '-';
                } else {
                    signal = '_';
                }
            } else if (strcmp(type, "XOR") == 0) {
                if (signals[index_1][j] + signals[index_2][j] == 1){
                    signal = '-';
                } else {
                    signal = '_';
                }
            } else if (strcmp(type, "NAND") == 0) {
                if (signals[index_1][j] + signals[index_2][j] != 2){
                    signal = '-';
                } else {
                    signal = '_';
                }
            } else if (strcmp(type, "NOR") == 0) {
                if (signals[index_1][j] + signals[index_2][j] == 0){
                    signal = '-';
                } else {
                    signal = '_';
                }               
            } else if (strcmp(type, "NXOR") == 0) {
                if (signals[index_1][j] + signals[index_2][j] != 1){
                    signal = '-';
                } else {
                    signal = '_';
                }
            }

            output_signal[j] = signal;
        }

        output_signal[signal_len] = '\0';
        printf("%s %s\n", output_name, output_signal);
    }

    return 0;
}