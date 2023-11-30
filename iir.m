for i = 0:15:255
  n = i;
  k = 256;
  a = [(n-k) k];
  b = [0 n];
  [h,w] = freqz(b,a,2001);
  mag = abs(h);
  plot(w/pi,20*log10(mag))
  grid on
  xlabel('Normalized Frequency (rad/s)')
  ylabel('dB')
  hold on
end
