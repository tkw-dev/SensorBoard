%coefficient
a = [0 0 0 4];
b = [1 1 1 1];

%nyquest frequency
ts = 5*10^(-3);
fn = 1/ts;

%plot frequency
fmin = 0*10^6;
fmax = 11*10^2;
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
