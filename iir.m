for i = 0:10:128
  %coefficient
  n = i;
  k = 256;
  a = [(n-k) k];
  b = [0 n];

  %nyquest frequency
  ts = 6*10^(-3);
  fn = 1/ts;

  %plot frequency
  fmin = 0.09*10^6;
  fmax = 0.11*10^6;
  Rmin = pi*fmin/fn;
  Rmax = pi*fmax/fn;
  resln = 1000;
  w = Rmin:pi/resln:Rmax;

  %transfer function
  h = freqz(b,a,w);

  %plot
  mag = abs(h);
  plot(fn*w/pi,20*log10(mag))
  grid on
  xlabel('Frequency (Hz)')
  ylabel('dB')
  hold on
end
