ans = 1;
n = 1;
for (d = 2; d < 1001; d += 2) {
  for (k = 0; k < 4; k++) {
    n = n + d;
    ans = ans + n;
  }
}
document.write('ANS: ', ans);