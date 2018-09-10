<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet version="1.0"
xmlns:xsl="http://www.w3.org/1999/XSL/Transform">

<xsl:output method="text" indent="yes" omit-xml-declaration="yes" />

<xsl:variable name='base_uri'>
	<xsl:text>http://www.ua.pt/ensino/uc/2380/projeto2/</xsl:text>
</xsl:variable>

<xsl:variable name='newline'>
	<xsl:text>&#xa;</xsl:text>
</xsl:variable>

<xsl:template match="/">
<xsl:for-each select="countries/country">
	<xsl:if test="name != ''">
		<xsl:value-of select="concat('&lt;', $base_uri, 'country/', position(), '&gt; ')"/>
		<xsl:value-of select="concat('&lt;', $base_uri, 'countryProperty/1', '&gt; ')"/>
		<xsl:value-of select="concat('&quot;', name, '&quot;', ' .', $newline)"/>
	</xsl:if>
	<xsl:if test="area != ''">
		<xsl:value-of select="concat('&lt;', $base_uri, 'country/', position(), '&gt; ')"/>
		<xsl:value-of select="concat('&lt;', $base_uri, 'countryProperty/2', '&gt; ')"/>
		<xsl:value-of select="concat(area, ' .', $newline)"/>
	</xsl:if>
	<xsl:if test="birthrate != ''">
		<xsl:value-of select="concat('&lt;', $base_uri, 'country/', position(), '&gt; ')"/>
		<xsl:value-of select="concat('&lt;', $base_uri, 'countryProperty/3', '&gt; ')"/>
		<xsl:value-of select="concat(birthrate, ' .', $newline)"/>
	</xsl:if>
	<xsl:if test="accountbalance != ''">
		<xsl:value-of select="concat('&lt;', $base_uri, 'country/', position(), '&gt; ')"/>
		<xsl:value-of select="concat('&lt;', $base_uri, 'countryProperty/4', '&gt; ')"/>
		<xsl:value-of select="concat(accountbalance, ' .', $newline)"/>
	</xsl:if>
	<xsl:if test="deathrate != ''">
		<xsl:value-of select="concat('&lt;', $base_uri, 'country/', position(), '&gt; ')"/>
		<xsl:value-of select="concat('&lt;', $base_uri, 'countryProperty/5', '&gt; ')"/>
		<xsl:value-of select="concat(deathrate, ' .', $newline)"/>
	</xsl:if>
	<xsl:if test="debt != ''">
		<xsl:value-of select="concat('&lt;', $base_uri, 'country/', position(), '&gt; ')"/>
		<xsl:value-of select="concat('&lt;', $base_uri, 'countryProperty/6', '&gt; ')"/>
		<xsl:value-of select="concat(debt, ' .', $newline)"/>
	</xsl:if>
	<xsl:if test="electricity_consumption != ''">
		<xsl:value-of select="concat('&lt;', $base_uri, 'country/', position(), '&gt; ')"/>
		<xsl:value-of select="concat('&lt;', $base_uri, 'countryProperty/7', '&gt; ')"/>
		<xsl:value-of select="concat(electricity_consumption, ' .', $newline)"/>
	</xsl:if>
	<xsl:if test="electricity_production != ''">
		<xsl:value-of select="concat('&lt;', $base_uri, 'country/', position(), '&gt; ')"/>
		<xsl:value-of select="concat('&lt;', $base_uri, 'countryProperty/8', '&gt; ')"/>
		<xsl:value-of select="concat(electricity_production, ' .', $newline)"/>
	</xsl:if>
	<xsl:if test="exports != ''">
		<xsl:value-of select="concat('&lt;', $base_uri, 'country/', position(), '&gt; ')"/>
		<xsl:value-of select="concat('&lt;', $base_uri, 'countryProperty/9', '&gt; ')"/>
		<xsl:value-of select="concat(exports, ' .', $newline)"/>
	</xsl:if>
	<xsl:if test="gdp != ''">
		<xsl:value-of select="concat('&lt;', $base_uri, 'country/', position(), '&gt; ')"/>
		<xsl:value-of select="concat('&lt;', $base_uri, 'countryProperty/10', '&gt; ')"/>
		<xsl:value-of select="concat(gdp, ' .', $newline)"/>
	</xsl:if>
	<xsl:if test="gdp_capita != ''">
		<xsl:value-of select="concat('&lt;', $base_uri, 'country/', position(), '&gt; ')"/>
		<xsl:value-of select="concat('&lt;', $base_uri, 'countryProperty/11', '&gt; ')"/>
		<xsl:value-of select="concat(gdp_capita, ' .', $newline)"/>
	</xsl:if>
	<xsl:if test="gdp_realgrowth != ''">
		<xsl:value-of select="concat('&lt;', $base_uri, 'country/', position(), '&gt; ')"/>
		<xsl:value-of select="concat('&lt;', $base_uri, 'countryProperty/12', '&gt; ')"/>
		<xsl:value-of select="concat(gdp_realgrowth, ' .', $newline)"/>
	</xsl:if>
	<xsl:if test="hiv_adultrate != ''">
		<xsl:value-of select="concat('&lt;', $base_uri, 'country/', position(), '&gt; ')"/>
		<xsl:value-of select="concat('&lt;', $base_uri, 'countryProperty/13', '&gt; ')"/>
		<xsl:value-of select="concat(hiv_adultrate, ' .', $newline)"/>
	</xsl:if>
	<xsl:if test="hiv_deaths != ''">
		<xsl:value-of select="concat('&lt;', $base_uri, 'country/', position(), '&gt; ')"/>
		<xsl:value-of select="concat('&lt;', $base_uri, 'countryProperty/14', '&gt; ')"/>
		<xsl:value-of select="concat(hiv_deaths, ' .', $newline)"/>
	</xsl:if>
	<xsl:if test="hiv_livingwith != ''">
		<xsl:value-of select="concat('&lt;', $base_uri, 'country/', position(), '&gt; ')"/>
		<xsl:value-of select="concat('&lt;', $base_uri, 'countryProperty/15', '&gt; ')"/>
		<xsl:value-of select="concat(hiv_livingwith, ' .', $newline)"/>
	</xsl:if>
	<xsl:if test="highways != ''">
		<xsl:value-of select="concat('&lt;', $base_uri, 'country/', position(), '&gt; ')"/>
		<xsl:value-of select="concat('&lt;', $base_uri, 'countryProperty/16', '&gt; ')"/>
		<xsl:value-of select="concat(highways, ' .', $newline)"/>
	</xsl:if>
	<xsl:if test="imports != ''">
		<xsl:value-of select="concat('&lt;', $base_uri, 'country/', position(), '&gt; ')"/>
		<xsl:value-of select="concat('&lt;', $base_uri, 'countryProperty/17', '&gt; ')"/>
		<xsl:value-of select="concat(imports, ' .', $newline)"/>
	</xsl:if>
	<xsl:if test="industrial_prod_growth_rate != ''">
		<xsl:value-of select="concat('&lt;', $base_uri, 'country/', position(), '&gt; ')"/>
		<xsl:value-of select="concat('&lt;', $base_uri, 'countryProperty/18', '&gt; ')"/>
		<xsl:value-of select="concat(industrial_prod_growth_rate, ' .', $newline)"/>
	</xsl:if>
	<xsl:if test="infant_mortality_rate != ''">
		<xsl:value-of select="concat('&lt;', $base_uri, 'country/', position(), '&gt; ')"/>
		<xsl:value-of select="concat('&lt;', $base_uri, 'countryProperty/19', '&gt; ')"/>
		<xsl:value-of select="concat(infant_mortality_rate, ' .', $newline)"/>
	</xsl:if>
	<xsl:if test="inflation_rate != ''">
		<xsl:value-of select="concat('&lt;', $base_uri, 'country/', position(), '&gt; ')"/>
		<xsl:value-of select="concat('&lt;', $base_uri, 'countryProperty/20', '&gt; ')"/>
		<xsl:value-of select="concat(inflation_rate, ' .', $newline)"/>
	</xsl:if>
	<xsl:if test="internet_hosts != ''">
		<xsl:value-of select="concat('&lt;', $base_uri, 'country/', position(), '&gt; ')"/>
		<xsl:value-of select="concat('&lt;', $base_uri, 'countryProperty/21', '&gt; ')"/>
		<xsl:value-of select="concat(internet_hosts, ' .', $newline)"/>
	</xsl:if>
	<xsl:if test="internet_users != ''">
		<xsl:value-of select="concat('&lt;', $base_uri, 'country/', position(), '&gt; ')"/>
		<xsl:value-of select="concat('&lt;', $base_uri, 'countryProperty/22', '&gt; ')"/>
		<xsl:value-of select="concat(internet_users, ' .', $newline)"/>
	</xsl:if>
	<xsl:if test="investment != ''">
		<xsl:value-of select="concat('&lt;', $base_uri, 'country/', position(), '&gt; ')"/>
		<xsl:value-of select="concat('&lt;', $base_uri, 'countryProperty/23', '&gt; ')"/>
		<xsl:value-of select="concat(investment, ' .', $newline)"/>
	</xsl:if>
	<xsl:if test="labor_force != ''">
		<xsl:value-of select="concat('&lt;', $base_uri, 'country/', position(), '&gt; ')"/>
		<xsl:value-of select="concat('&lt;', $base_uri, 'countryProperty/24', '&gt; ')"/>
		<xsl:value-of select="concat(labor_force, ' .', $newline)"/>
	</xsl:if>
	<xsl:if test="life_expectancy != ''">
		<xsl:value-of select="concat('&lt;', $base_uri, 'country/', position(), '&gt; ')"/>
		<xsl:value-of select="concat('&lt;', $base_uri, 'countryProperty/25', '&gt; ')"/>
		<xsl:value-of select="concat(life_expectancy, ' .', $newline)"/>
	</xsl:if>
	<xsl:if test="military_expenditures != ''">
		<xsl:value-of select="concat('&lt;', $base_uri, 'country/', position(), '&gt; ')"/>
		<xsl:value-of select="concat('&lt;', $base_uri, 'countryProperty/26', '&gt; ')"/>
		<xsl:value-of select="concat(military_expenditures, ' .', $newline)"/>
	</xsl:if>
	<xsl:if test="military_expenditures_gdp != ''">
		<xsl:value-of select="concat('&lt;', $base_uri, 'country/', position(), '&gt; ')"/>
		<xsl:value-of select="concat('&lt;', $base_uri, 'countryProperty/27', '&gt; ')"/>
		<xsl:value-of select="concat(military_expenditures_gdp, ' .', $newline)"/>
	</xsl:if>
	<xsl:if test="naturalGas_consumption != ''">
		<xsl:value-of select="concat('&lt;', $base_uri, 'country/', position(), '&gt; ')"/>
		<xsl:value-of select="concat('&lt;', $base_uri, 'countryProperty/28', '&gt; ')"/>
		<xsl:value-of select="concat(naturalGas_consumption, ' .', $newline)"/>
	</xsl:if>
	<xsl:if test="naturalGas_exports != ''">
		<xsl:value-of select="concat('&lt;', $base_uri, 'country/', position(), '&gt; ')"/>
		<xsl:value-of select="concat('&lt;', $base_uri, 'countryProperty/29', '&gt; ')"/>
		<xsl:value-of select="concat(naturalGas_exports, ' .', $newline)"/>
	</xsl:if>
	<xsl:if test="naturalGas_imports != ''">
		<xsl:value-of select="concat('&lt;', $base_uri, 'country/', position(), '&gt; ')"/>
		<xsl:value-of select="concat('&lt;', $base_uri, 'countryProperty/30', '&gt; ')"/>
		<xsl:value-of select="concat(naturalGas_imports, ' .', $newline)"/>
	</xsl:if>
	<xsl:if test="naturalGas_production != ''">
		<xsl:value-of select="concat('&lt;', $base_uri, 'country/', position(), '&gt; ')"/>
		<xsl:value-of select="concat('&lt;', $base_uri, 'countryProperty/31', '&gt; ')"/>
		<xsl:value-of select="concat(naturalGas_production, ' .', $newline)"/>
	</xsl:if>
	<xsl:if test="naturalGas_reserves != ''">
		<xsl:value-of select="concat('&lt;', $base_uri, 'country/', position(), '&gt; ')"/>
		<xsl:value-of select="concat('&lt;', $base_uri, 'countryProperty/32', '&gt; ')"/>
		<xsl:value-of select="concat(naturalGas_reserves, ' .', $newline)"/>
	</xsl:if>
	<xsl:if test="oil_consumption != ''">
		<xsl:value-of select="concat('&lt;', $base_uri, 'country/', position(), '&gt; ')"/>
		<xsl:value-of select="concat('&lt;', $base_uri, 'countryProperty/33', '&gt; ')"/>
		<xsl:value-of select="concat(oil_consumption, ' .', $newline)"/>
	</xsl:if>
	<xsl:if test="oil_exports != ''">
		<xsl:value-of select="concat('&lt;', $base_uri, 'country/', position(), '&gt; ')"/>
		<xsl:value-of select="concat('&lt;', $base_uri, 'countryProperty/34', '&gt; ')"/>
		<xsl:value-of select="concat(oil_exports, ' .', $newline)"/>
	</xsl:if>
	<xsl:if test="oil_imports != ''">
		<xsl:value-of select="concat('&lt;', $base_uri, 'country/', position(), '&gt; ')"/>
		<xsl:value-of select="concat('&lt;', $base_uri, 'countryProperty/35', '&gt; ')"/>
		<xsl:value-of select="concat(oil_imports, ' .', $newline)"/>
	</xsl:if>
	<xsl:if test="oil_production != ''">
		<xsl:value-of select="concat('&lt;', $base_uri, 'country/', position(), '&gt; ')"/>
		<xsl:value-of select="concat('&lt;', $base_uri, 'countryProperty/36', '&gt; ')"/>
		<xsl:value-of select="concat(oil_production, ' .', $newline)"/>
	</xsl:if>
	<xsl:if test="oil_reserves != ''">
		<xsl:value-of select="concat('&lt;', $base_uri, 'country/', position(), '&gt; ')"/>
		<xsl:value-of select="concat('&lt;', $base_uri, 'countryProperty/37', '&gt; ')"/>
		<xsl:value-of select="concat(oil_reserves, ' .', $newline)"/>
	</xsl:if>
	<xsl:if test="population != ''">
		<xsl:value-of select="concat('&lt;', $base_uri, 'country/', position(), '&gt; ')"/>
		<xsl:value-of select="concat('&lt;', $base_uri, 'countryProperty/38', '&gt; ')"/>
		<xsl:value-of select="concat(population, ' .', $newline)"/>
	</xsl:if>
	<xsl:if test="public_debt != ''">
		<xsl:value-of select="concat('&lt;', $base_uri, 'country/', position(), '&gt; ')"/>
		<xsl:value-of select="concat('&lt;', $base_uri, 'countryProperty/39', '&gt; ')"/>
		<xsl:value-of select="concat(public_debt, ' .', $newline)"/>
	</xsl:if>
	<xsl:if test="railways != ''">
		<xsl:value-of select="concat('&lt;', $base_uri, 'country/', position(), '&gt; ')"/>
		<xsl:value-of select="concat('&lt;', $base_uri, 'countryProperty/40', '&gt; ')"/>
		<xsl:value-of select="concat(railways, ' .', $newline)"/>
	</xsl:if>
	<xsl:if test="reserves_foreign_exchange_gold != ''">
		<xsl:value-of select="concat('&lt;', $base_uri, 'country/', position(), '&gt; ')"/>
		<xsl:value-of select="concat('&lt;', $base_uri, 'countryProperty/41', '&gt; ')"/>
		<xsl:value-of select="concat(reserves_foreign_exchange_gold, ' .', $newline)"/>
	</xsl:if>
	<xsl:if test="telephones_main_lines != ''">
		<xsl:value-of select="concat('&lt;', $base_uri, 'country/', position(), '&gt; ')"/>
		<xsl:value-of select="concat('&lt;', $base_uri, 'countryProperty/42', '&gt; ')"/>
		<xsl:value-of select="concat(telephones_main_lines, ' .', $newline)"/>
	</xsl:if>
	<xsl:if test="telephones_mobile_cellular != ''">
		<xsl:value-of select="concat('&lt;', $base_uri, 'country/', position(), '&gt; ')"/>
		<xsl:value-of select="concat('&lt;', $base_uri, 'countryProperty/43', '&gt; ')"/>
		<xsl:value-of select="concat(telephones_mobile_cellular, ' .', $newline)"/>
	</xsl:if>
	<xsl:if test="total_fertility_rate != ''">
		<xsl:value-of select="concat('&lt;', $base_uri, 'country/', position(), '&gt; ')"/>
		<xsl:value-of select="concat('&lt;', $base_uri, 'countryProperty/44', '&gt; ')"/>
		<xsl:value-of select="concat(total_fertility_rate, ' .', $newline)"/>
	</xsl:if>
	<xsl:if test="unemployment_rate != ''">
		<xsl:value-of select="concat('&lt;', $base_uri, 'country/', position(), '&gt; ')"/>
		<xsl:value-of select="concat('&lt;', $base_uri, 'countryProperty/45', '&gt; ')"/>
		<xsl:value-of select="concat(unemployment_rate, ' .', $newline)"/>
	</xsl:if>
</xsl:for-each>
</xsl:template>
</xsl:stylesheet>